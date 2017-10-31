import ast
import sys
import traceback

from ..java import opcodes as JavaOpcodes
from .modules import Module
from .methods import MainFunction, InitMethod, to_java
from .structures import (
    IF, ELSE, END_IF,
    TRY, CATCH, FINALLY, END_TRY,
    START_LOOP, END_LOOP,
    ArgType,
    jump, OpcodePosition,
    AddToArgs, AddToKwargs
)
from .types.primitives import (
    ASTORE_name, ALOAD_name, free_name,
    ICONST_val, ISTORE_name, ILOAD_name
)
from .types import java, python
from .debug import (
    dump,
    # DEBUG, DEBUG_name
)


def is_call(node, name):
    return (
        # Node is a Call statement...
        isinstance(node, ast.Call)
        # ... where the function being invoked ...
        and isinstance(node.func, ast.Name)
        # ... is the provided name
        and (
            (isinstance(name, str) and node.func.id == name)
            or (isinstance(name, tuple) and node.func.id in name)
        )
    )


def node_visitor(fn):
    def dec(self, node, *args, **kwargs):
        try:
            if node.lineno != self._current_line:
                self._current_line = self.context.next_opcode_starts_line = node.lineno
        except AttributeError:
            pass
        self.context.next_resolve_list.append((node, OpcodePosition.START))
        fn(self, node, *args, **kwargs)
        self.context.next_resolve_list.append((node, OpcodePosition.END))
        self.context.next_resolve_list.append((node, OpcodePosition.NEXT))
    return dec


class NameVisitor(ast.NodeVisitor):
    def evaluate(self, root_node):
        self.names = [[]]
        if root_node:
            self.visit(root_node)
        return self

    @property
    def cls_name(self):
        return '$'.join('.'.join(n for n in group if n) for group in self.names)

    @property
    def ref_name(self):
        return '$'.join('/'.join(n for n in group if n) for group in self.names)

    @property
    def annotation(self):
        type_name = self.ref_name
        return type_name if type_name else 'org/python/Object'

    def visit_Name(self, node):
        self.names[-1].append(node.id)

    def visit_NameConstant(self, node):
        if node.value is None:
            self.names[-1].append("void")
        else:
            raise NotImplementedError("Unknown named constant %s" % node.value)

    def visit_Attribute(self, node):
        self.visit(node.value)
        self.names[-1].append(node.attr)

    def visit_Subscript(self, node):
        self.visit(node.value)
        self.names.append([])
        self.visit(node.slice)

    def visit_Index(self, node):
        self.visit(node.value)


class LocalsVisitor(ast.NodeVisitor):
    def __init__(self, context):
        self.context = context

    def visit_Name(self, node):
        if type(node.ctx) == ast.Store:
            if node.id not in self.context.local_vars:
                self.context.local_vars[node.id] = None

    def visit_Attribute(self, node):
        pass


class Visitor(ast.NodeVisitor):
    def __init__(self, namespace, filename, verbosity=1):
        super().__init__()
        self.namespace = namespace
        self.filename = filename
        self.verbosity = verbosity

        self._current_line = None
        self._context = []
        self._root_module = None

        self.current_exc_name = []

        self.symbol_namespace = {}
        self.code_objects = {}

    @property
    def context(self):
        return self._context[-1]

    @property
    def root_module(self):
        return self._root_module

    def push_context(self, block):
        self._context.append(block)
        block.visitor_setup()

    def pop_context(self):
        self.context.visitor_teardown()
        self._context.pop()

    def full_classref(self, name, default_prefix=None):
        return self.symbol_namespace.get(name, '.'.join([default_prefix, name])).replace('.', '/')

    def extract_code_objects(self, compiled):
        for obj in compiled.co_consts:
            if isinstance(obj, type(compiled)):
                if (obj.co_firstlineno, obj.co_name) in self.code_objects:
                    print(
                        'WARNING: multiple %s code objects found on line %s' % (
                            obj.co_name, obj.co_firstlineno
                        ),
                        file=sys.stderr
                    )
                self.code_objects[(obj.co_firstlineno, obj.co_name)] = obj
                self.extract_code_objects(obj)

    def visit(self, node):
        try:
            super().visit(node)
        except Exception as e:
            traceback.print_exc()
            print()
            print("Problem occurred in %s" % self.filename)
            print('Node: %s' % dump(node))
            sys.exit(1)
        return self._root_module

    def visit_Module(self, node):
        # Compile the module, and extract all the code objects
        compiled = compile(node, filename=self.filename, mode='exec')
        self.extract_code_objects(compiled)

        module = Module(self.namespace, self.filename)
        self.push_context(module)

        if self._root_module is None:
            self._root_module = module

        for child in node.body:
            self.visit(child)

        main = MainFunction(module)
        self.push_context(main)
        # No content, so pop right away.
        # We need to push to make sure setup/teardown
        # logic is invoked.
        self.pop_context()

        module.functions.append(main)

        self.pop_context()

    @node_visitor
    def visit_Interactive(self, node):
        # stmt* body):
        raise NotImplementedError('No handler for Interactive')

    @node_visitor
    def visit_Expr(self, node):
        self.generic_visit(node)

        # If the expression is a call, we need to ignore
        # any return value from the function.
        if isinstance(node.value, (ast.Call, ast.Attribute, ast.Str)):
            self.context.add_opcodes(
                JavaOpcodes.POP()
            )

    @node_visitor
    def visit_Suite(self, node):
        # stmt* body):
        raise NotImplementedError('No handler for Suite')

    # Statements
    @node_visitor
    def visit_FunctionDef(self, node):
        function = self._create_function(node, node.name, node.decorator_list)

        self.push_context(function)

        LocalsVisitor(function).visit(node)

        for child in node.body:
            self.visit(child)
        self.pop_context()

    @node_visitor
    def visit_ClassDef(self, node):
        # Construct a class.
        class_name = node.name

        name_visitor = NameVisitor()

        extends = None
        implements = []

        for keyword in node.keywords:
            key = keyword.arg
            value = keyword.value

            if key == "metaclass":
                raise Exception("Can't handle metaclasses")
            elif key == "extends":
                extends = name_visitor.evaluate(value).ref_name
            elif key == "implements":
                if isinstance(value, ast.List):
                    implements = [
                        name_visitor.visit(v).ref_name
                        for v in value.elts
                    ]
                else:
                    implements = [name_visitor.evaluate(value).ref_name]
            else:
                raise Exception("Unknown meta keyword " + str(key))

        self.context.add_opcodes(
            java.List(),
        )

        if extends:
            first_base = extends
        elif not node.bases:
            first_base = 'org/python/types/Object'
        else:
            first_base = None

        if first_base:
            self.context.add_opcodes(
                JavaOpcodes.DUP(),
                python.Type.for_class(first_base),
                java.List.add(),
            )

        for base in node.bases:
            self.context.add_opcodes(
                JavaOpcodes.DUP(),
            )
            self.visit(base)
            self.context.add_opcodes(
                java.List.add(),
            )

        klass = self.context.add_class(class_name, extends, implements)

        self.push_context(klass)
        for child in node.body:
            self.visit(child)
        self.pop_context()

        self.symbol_namespace[class_name] = klass.class_name

    @node_visitor
    def visit_Return(self, node):
        # expr? value):
        if node.value:
            self.visit(node.value)
        else:
            self.context.add_opcodes(python.NONE())
        self.context.add_opcodes(JavaOpcodes.ARETURN())
        # Record how deep we were when this return was added.
        self.context.opcodes[-1].needs_implicit_return = \
            self.context.has_nested_structure

    @node_visitor
    def visit_Delete(self, node):
        for target in node.targets:
            self.visit(target)
            if isinstance(target, ast.Attribute):
                self.context.add_opcodes(
                    python.Object.del_attr()
                )
            elif isinstance(target, ast.Subscript):
                self.context.add_opcodes(
                    python.Object.del_item()
                )
            elif isinstance(target, ast.Name):
                # delete is performed by visit(target) with context Del
                pass
            else:
                raise NotImplementedError('No handler for Delete of type %s' % target)

    @node_visitor
    def visit_Assign(self, node):
        # Evaluate the value
        self.visit(node.value)

        if len(node.targets) > 1:
            for target in node.targets:
                # Assign the value to the target
                self.context.add_opcodes(
                    JavaOpcodes.DUP()
                )
                self.visit(target)
            self.context.add_opcodes(
                JavaOpcodes.POP()
            )
        else:
            self.visit(node.targets[0])

    @node_visitor
    def visit_AugAssign(self, node):
        # expr target, operator op, expr value):

        # Evaluate the target
        if isinstance(node.target, ast.Subscript):
            self.visit_Subscript(node.target, ctx=ast.Load())
        elif isinstance(node.target, ast.Attribute):
            self.visit_Attribute(node.target, ctx=ast.Load())
        else:
            self.context.load_name(node.target.id)

        # Evaluate the value
        self.visit(node.value)
        self.context.add_opcodes(
            JavaOpcodes.INVOKEINTERFACE(
                'org/python/Object',
                {
                    ast.Add: '__iadd__',
                    ast.Sub: '__isub__',
                    ast.Mult: '__imul__',
                    ast.Div: '__itruediv__',
                    ast.FloorDiv: '__ifloordiv__',
                    ast.Mod: '__imod__',
                    ast.Pow: '__ipow__',
                    ast.LShift: '__ilshift__',
                    ast.RShift: '__irshift__',
                    ast.BitOr: '__ior__',
                    ast.BitXor: '__ixor__',
                    ast.BitAnd: '__iand__',
                    # ast.MatMult: '__imatmult__',
                }[type(node.op)],
                args=['Lorg/python/Object;'],
                returns='Lorg/python/Object;'
            )
        )
        self.visit(node.target)

    @node_visitor
    def visit_For(self, node):
        self.visit(node.iter)
        self.context.add_opcodes(
            python.Object.iter()
        )

        loop = START_LOOP()

        self.context.add_opcodes(
            JavaOpcodes.ICONST_1(),
            ISTORE_name('#loop-orelse-%x' % id(loop)),
        )
        self.context.store_name('#for-iter-%x' % id(node), declare=True)
        self.context.add_opcodes(
            loop,
        )
        self.context.add_opcodes(
                TRY(),
        )
        self.context.load_name('#for-iter-%x' % id(node)),
        self.context.add_opcodes(
                    python.Iterable.next(),
        )
        self.context.add_opcodes(
                CATCH('org/python/exceptions/StopIteration'),
        )
        self.context.add_opcodes(
                    JavaOpcodes.POP(),
                    jump(JavaOpcodes.GOTO(0), self.context, loop, OpcodePosition.NEXT),
        )
        self.context.add_opcodes(
                END_TRY(),
        )

        self.visit(node.target)

        for child in node.body:
            self.visit(child)

        self.context.add_opcodes(
            END_LOOP()
        )

        if node.orelse:
            self.context.add_opcodes(
                ILOAD_name('#loop-orelse-%x' % id(loop)),
                IF([], JavaOpcodes.IFEQ)
            )
            for child in node.orelse:
                self.visit(child)
            self.context.add_opcodes(
                END_IF()
            )

        # Clean up
        self.context.delete_name('#for-iter-%x' % id(node))

    @node_visitor
    def visit_While(self, node):
        # expr test, stmt* body, stmt* orelse):

        loop = START_LOOP()

        self.context.add_opcodes(
            JavaOpcodes.ICONST_1(),
            ISTORE_name('#loop-orelse-%x' % id(loop)),
        )

        self.context.add_opcodes(
            loop
        )
        self.visit(node.test)
        self.context.add_opcodes(
            IF([python.Object.as_boolean()], JavaOpcodes.IFNE),
        )
        self.context.add_opcodes(
                jump(JavaOpcodes.GOTO(0), self.context, loop, OpcodePosition.NEXT),
        )
        self.context.add_opcodes(
            END_IF(),
        )

        for child in node.body:
            self.visit(child)

        self.context.add_opcodes(
            END_LOOP()
        )

        if node.orelse:
            self.context.add_opcodes(
                ILOAD_name('#loop-orelse-%x' % id(loop)),
                IF([], JavaOpcodes.IFEQ)
            )
            for child in node.orelse:
                self.visit(child)
            self.context.add_opcodes(
                END_IF()
            )

    @node_visitor
    def visit_If(self, node):
        # expr test, stmt* body, stmt* orelse):
        self.visit(node.test)

        self.context.add_opcodes(
            IF([python.Object.as_boolean()], JavaOpcodes.IFEQ),
        )

        for child in node.body:
            self.visit(child)

        if node.orelse:
            self.context.add_opcodes(
                ELSE(),
            )

            for child in node.orelse:
                self.visit(child)

        self.context.add_opcodes(
            END_IF()
        )

    @node_visitor
    def visit_With(self, node):
        # withitem* items, stmt* body):
        #     withitem = (expr context_expr, expr? optional_vars)
        exit_names = ['#exit-%d-%x' % (i, id(node)) for i, _ in enumerate(node.items)]

        for i, item in enumerate(node.items):
            self.visit(item.context_expr)

            self.context.add_opcodes(
                JavaOpcodes.DUP(),
                python.Object.get_attribute('__exit__', use_null=True),
                JavaOpcodes.DUP(),
                ASTORE_name(exit_names[i]),
                IF([], JavaOpcodes.IFNONNULL),
                java.THROW(
                    'org/python/exceptions/AttributeError',
                    ['Ljava/lang/String;', JavaOpcodes.LDC_W('__exit__')]
                ),
                END_IF(),
            )

            self.context.add_opcodes(
                python.Object.get_attribute('__enter__', use_null=True),
                JavaOpcodes.DUP(),
                IF([], JavaOpcodes.IFNONNULL),
                java.THROW(
                    'org/python/exceptions/AttributeError',
                    ['Ljava/lang/String;', JavaOpcodes.LDC_W('__enter__')]
                ),
                END_IF(),
            )

            self.context.add_opcodes(
                JavaOpcodes.ACONST_NULL(),
                JavaOpcodes.ACONST_NULL(),
                python.Callable.invoke(),
            )

            if item.optional_vars:
                self.context.store_name(item.optional_vars.id)
            else:
                self.context.add_opcodes(
                    JavaOpcodes.POP(),
                )

        self.context.add_opcodes(
            TRY(),
        )

        for child in node.body:
            self.visit(child)

        for name in exit_names[::-1]:
            self.context.add_opcodes(
                ALOAD_name(name),
            )
            self.context.add_opcodes(java.Array(3, fill=python.NONE()))
            self.context.add_opcodes(
                JavaOpcodes.ACONST_NULL(),
                python.Callable.invoke(),
                JavaOpcodes.POP(),
            )

        self.context.add_opcodes(
            CATCH('org/python/exceptions/Exception'),
            ASTORE_name('#exception-%x' % id(node)),
        )

        for name in exit_names[::-1]:
            self.context.add_opcodes(
                ALOAD_name(name),
            )
            self.context.add_opcodes(
                java.Array(3),
                JavaOpcodes.DUP(),
                ICONST_val(0),
                python.NONE(),  # TODO: pass the exception type here
                JavaOpcodes.AASTORE(),
                JavaOpcodes.DUP(),
                ICONST_val(1),
                ALOAD_name('#exception-%x' % id(node)),
                JavaOpcodes.AASTORE(),
                JavaOpcodes.DUP(),
                ICONST_val(2),
                python.NONE(),  # TODO: pass the traceback info here
                JavaOpcodes.AASTORE(),
            ),
            self.context.add_opcodes(
                JavaOpcodes.ACONST_NULL(),
                python.Callable.invoke(),
                JavaOpcodes.POP(),
            )

        self.context.add_opcodes(
            ALOAD_name('#exception-%x' % id(node)),
            JavaOpcodes.ATHROW(),
            END_TRY(),
            free_name('#exception-%x' % id(node)),
        )
        for name in exit_names:
            self.context.add_opcodes(free_name(name))

    @node_visitor
    def visit_Raise(self, node):
        if node.exc is None:
            # Re-raise most recent exception.
            self.context.add_opcodes(
                ALOAD_name(self.current_exc_name[-1]),
            )
        else:
            if getattr(node.exc, 'func', None) is not None:
                name = node.exc.func.id
                args = node.exc.args
            else:
                name = node.exc.id
                args = []

            exception = self.full_classref(name, default_prefix='org.python.exceptions')
            self.context.add_opcodes(
                java.New(exception),
            )

            for arg in args:
                self.visit(arg)

            self.context.add_opcodes(
                java.Init(exception, *(['Lorg/python/Object;'] * len(args)))
            )

        self.context.add_opcodes(
            JavaOpcodes.ATHROW(),
        )

    @node_visitor
    def visit_Try(self, node):
        # stmt* body, excepthandler* handlers, stmt* orelse, stmt* finalbody):
        self.context.add_opcodes(
            TRY()
        )

        for child in node.body:
            self.visit(child)

        for child in node.orelse:
            self.visit(child)

        # Finally content is duplicated at the end of the body
        # if it is defined.
        if node.finalbody:
            for child in node.finalbody:
                self.visit(child)

        for handler in node.handlers:
            self.visit(handler)

            # Finally content is duplicated at the end of the handler
            # if it is defined.
            if node.finalbody:
                for child in node.finalbody:
                    self.visit(child)

        if node.finalbody:
            self.context.add_opcodes(
                FINALLY(),
                ASTORE_name('#exception-%x' % id(node))
            )

            for child in node.finalbody:
                self.visit(child)

            self.context.add_opcodes(
                ALOAD_name('#exception-%x' % id(node)),
                JavaOpcodes.ATHROW(),
                free_name('#exception-%x' % id(node))
            )

        self.context.add_opcodes(
            END_TRY()
        )

    @node_visitor
    def visit_Assert(self, node):
        self.visit(node.test)
        self.context.add_opcodes(
            IF([python.Object.as_boolean()], JavaOpcodes.IFNE),
        )
        self.context.add_opcodes(
                java.New('org/python/exceptions/AssertionError'),
        )

        if node.msg:
            self.visit(node.msg)
            self.context.add_opcodes(
                    java.Init('org/python/exceptions/AssertionError', 'Lorg/python/Object;'),
            )
        else:
            self.context.add_opcodes(
                    java.Init('org/python/exceptions/AssertionError'),
            )

        self.context.add_opcodes(
                JavaOpcodes.ATHROW(),
        )
        self.context.add_opcodes(
            END_IF(),
        )

    @node_visitor
    def visit_Import(self, node):
        for alias in node.names:
            self.context.add_opcodes(
                JavaOpcodes.LDC_W(alias.name),
            )
            self.context.load_globals()
            self.context.load_locals()
            self.context.add_opcodes(
                JavaOpcodes.ACONST_NULL(),  # from_list
                JavaOpcodes.ICONST_0(),
                JavaOpcodes.INVOKESTATIC(
                    'org/python/ImportLib',
                    '__import__',
                    args=[
                        'Ljava/lang/String;',
                        'Ljava/util/Map;',
                        'Ljava/util/Map;',
                        '[Ljava/lang/String;',
                        'I',
                    ],
                    returns='Lorg/python/types/Module;'
                )
            )
            if alias.asname:
                self.context.store_name(alias.asname)
            else:
                # The alias will be the fully dotted path. The import
                # will return the top level module. Store the top level
                # module as the top level path.
                self.context.store_name(alias.name.split('.')[0])

    @node_visitor
    def visit_ImportFrom(self, node):
        if node.module:
            self.context.add_opcodes(
                JavaOpcodes.LDC_W(node.module),
            )
        else:
            self.context.add_opcodes(
                JavaOpcodes.ACONST_NULL(),
            )

        self.context.load_globals()
        self.context.load_locals()

        self.context.add_opcodes(
            java.Array(len(node.names), 'java/lang/String'),
        )

        for i, alias in enumerate(node.names):
            self.context.add_opcodes(
                JavaOpcodes.DUP(),
                ICONST_val(i),
                JavaOpcodes.LDC_W(alias.name),
                JavaOpcodes.AASTORE(),
            )

        self.context.add_opcodes(
            ICONST_val(node.level),
            JavaOpcodes.INVOKESTATIC(
                'org/python/ImportLib',
                '__import__',
                args=[
                    'Ljava/lang/String;',
                    'Ljava/util/Map;',
                    'Ljava/util/Map;',
                    '[Ljava/lang/String;',
                    'I',
                ],
                returns='Lorg/python/types/Module;'
            )
        )

        if len(node.names) == 1 and node.names[0].name == '*':
            # Find exported symbols (__all__, or everything but private "_" symbols)
            self.context.add_opcodes(
                JavaOpcodes.INVOKESTATIC(
                    'org/python/ImportLib',
                    'importAll',
                    args=['Lorg/python/types/Module;'],
                    returns='Ljava/util/Map;'
                )
            )

            # Add all the exported symbols to the currrent context
            self.context.store_dynamic()
        else:
            for alias in node.names:
                self.context.add_opcodes(
                    JavaOpcodes.DUP(),
                    python.Object.get_attribute(alias.name),
                )

                if alias.asname:
                    self.context.store_name(alias.asname)
                else:
                    self.context.store_name(alias.name)

            self.context.add_opcodes(
                JavaOpcodes.POP(),
            )

    @node_visitor
    def visit_Global(self, node):
        for name in node.names:
            self.context.local_vars.pop(name, None)

    @node_visitor
    def visit_Nonlocal(self, node):
        # identifier* names):
        raise NotImplementedError('No handler for Nonlocal')

    @node_visitor
    def visit_Pass(self, node):
        pass

    @node_visitor
    def visit_Break(self, node):
        for loop in self.context.loops[::-1]:
            if loop.end_op is None:
                break

        self.context.add_opcodes(
            JavaOpcodes.ICONST_0(),
            ISTORE_name('#loop-orelse-%x' % id(loop)),
        )
        self.context.add_opcodes(
            jump(JavaOpcodes.GOTO(0), self.context, loop, OpcodePosition.NEXT),
        )

    @node_visitor
    def visit_Continue(self, node):
        for loop in self.context.loops[::-1]:
            if loop.end_op is None:
                break
        self.context.add_opcodes(
            jump(JavaOpcodes.GOTO(0), self.context, loop, OpcodePosition.START),
        )

    # # Expressions
    @node_visitor
    def visit_BoolOp(self, node):
        # boolop op, expr* values):
        comparison = {
            ast.Or: JavaOpcodes.IFNE,
            ast.And: JavaOpcodes.IFEQ,
        }[type(node.op)]

        for child in node.values[:-1]:
            self.visit(child)

            self.context.add_opcodes(
                # Duplicate the value found by the child, and evaluate
                # it's truthiness. If it matches the boolean operation,
                # we've found a match; jump to the end.
                JavaOpcodes.DUP(),
                python.Object.as_boolean(),
                jump(comparison(0), self.context, node, OpcodePosition.END),

                # This value wasn't a match; pop it off the stack.
                JavaOpcodes.POP(),
            )
        # The last value is the failsafe.
        self.visit(node.values[-1])

    @node_visitor
    def visit_BinOp(self, node):
        # expr left, operator op, expr right):
        if isinstance(node.op, ast.Pow):
            self.visit(node.left)
            self.visit(node.right)
            self.context.add_opcodes(
                JavaOpcodes.ACONST_NULL(),
                JavaOpcodes.INVOKEINTERFACE(
                    'org/python/Object',
                    '__pow__',
                    args=['Lorg/python/Object;', 'Lorg/python/Object;'],
                    returns='Lorg/python/Object;'
                ),
            )
        else:
            self.visit(node.left)
            self.visit(node.right)
            self.context.add_opcodes(
                JavaOpcodes.INVOKEINTERFACE(
                    'org/python/Object',
                    {
                        ast.Add: '__add__',
                        ast.Sub: '__sub__',
                        ast.Mult: '__mul__',
                        ast.Div: '__truediv__',
                        ast.FloorDiv: '__floordiv__',
                        ast.Mod: '__mod__',
                        ast.Pow: '__pow__',
                        ast.LShift: '__lshift__',
                        ast.RShift: '__rshift__',
                        ast.BitOr: '__or__',
                        ast.BitXor: '__xor__',
                        ast.BitAnd: '__and__',
                        # ast.MatMult:
                    }[type(node.op)],
                    args=['Lorg/python/Object;'],
                    returns='Lorg/python/Object;'
                )
            )

    @node_visitor
    def visit_UnaryOp(self, node):
        self.visit(node.operand)
        self.context.add_opcodes(
            JavaOpcodes.INVOKEINTERFACE(
                'org/python/Object',
                {
                    ast.USub: '__neg__',
                    ast.UAdd: '__pos__',
                    ast.Not: '__not__',
                    ast.Invert: '__invert__',
                }[type(node.op)],
                args=[],
                returns='Lorg/python/Object;'
            )
        )

    def _create_function(self, node, func_name, decorator_list):
        name_visitor = NameVisitor()
        default_vars = []
        parameter_signatures = []
        arg_index = {}
        for i, arg in enumerate(node.args.args):
            index = len(node.args.defaults) - len(node.args.args) + i
            if index != 0:
                # Store the index of the arguments; this is only used by
                # the @super decorator on the constructors.
                # self can be ignored.
                arg_index[arg.arg] = i - 1
            if index >= 0:
                default = '#%s-default-%s-%x' % (func_name, i, id(node))
                self.visit(node.args.defaults[index])
                self.context.add_opcodes(
                    ASTORE_name(default)
                )
                default_vars.append(default)
            else:
                default = None

            parameter_signatures.append({
                'name': arg.arg,
                'annotation': name_visitor.evaluate(arg.annotation).annotation,
                'kind': ArgType.POSITIONAL_OR_KEYWORD,
                'default': default
            })

        if node.args.vararg:
            arg_index[node.args.vararg] = len(node.args.args)
            parameter_signatures.append({
                'name': node.args.vararg.arg,
                'annotation': name_visitor.evaluate(node.args.vararg.annotation).annotation,
                'kind': ArgType.VAR_POSITIONAL,
            })

        for i, arg in enumerate(node.args.kwonlyargs):
            index = len(node.args.kw_defaults) - len(node.args.kwonlyargs) + i
            arg_index[arg.arg] = None
            if index >= 0 and node.args.kw_defaults[index] is not None:
                default = '#%s-kw_default-%s-%x' % (func_name, i, id(node))
                self.visit(node.args.kw_defaults[index])
                self.context.add_opcodes(
                    ASTORE_name(default)
                )
                default_vars.append(default)
            else:
                default = None

            parameter_signatures.append({
                'name': arg.arg,
                'annotation': name_visitor.evaluate(arg.annotation).annotation,
                'kind': ArgType.KEYWORD_ONLY,
                'default': default
            })

        if node.args.kwarg:
            arg_index[node.args.kwarg] = None
            parameter_signatures.append({
                'name': node.args.kwarg.arg,
                'annotation': name_visitor.evaluate(node.args.kwarg.annotation).annotation,
                'kind': ArgType.VAR_KEYWORD,
            })

        returns = getattr(node, 'returns', None)
        return_signature = {
            'annotation': name_visitor.evaluate(returns).annotation
        }

        # Now actually define the function.
        for decorator in decorator_list:
            # The @super decorator on __init__() is a special case. It tells us how
            # we want to invoke super() in the Java construction process.
            # It should have a single argument; a dictionary that has the
            # expressions to be passed in as arguments as keys, and the type
            # annotation for the argument as the value. For example:
            #
            #   class MyClass(BaseClass):
            #       @super({value: int, value*2: float, "Hello": java.lang.String})
            #       def __init__(self, value):
            #           ...
            #
            # would map to the rough equivalent of:
            #
            #   public MyClass(value) {
            #       super(value, value * 2, "Hello");
            #           ...
            #   }
            #
            if is_call(decorator, 'super'):
                if func_name == '__init__':
                    if len(decorator.args) == 1 and isinstance(decorator.args[0], ast.Dict):
                        super_args = [
                            name_visitor.evaluate(arg_type).ref_name
                            for arg_type in decorator.args[0].values
                        ]
                        init = InitMethod(
                            klass=self.context,
                            args=arg_index,
                            super_args=super_args,
                        )
                        self.push_context(init)

                        for arg, annotation in zip(decorator.args[0].keys, super_args):
                            self.visit(arg)
                            to_java(self.context, annotation)

                        self.pop_context()
                        self.context.constructor = init
                    else:
                        raise Exception("super() (as __init__ decorator) expects a single dictionary as an argument")
                else:
                    raise Exception("super() can only be used as a decorator on __init__()")
            elif isinstance(decorator, ast.Name) and decorator.id == "classmethod":
                # print("FIXME: Ignoring classmethod")
                pass
            elif isinstance(decorator, ast.Name) and decorator.id == "staticmethod":
                # print("FIXME: Ignoring staticmethod")
                pass
            else:
                self.visit(decorator)
                self.context.add_opcodes(
                    JavaOpcodes.CHECKCAST('org/python/Callable'),
                    java.Array(1),
                    JavaOpcodes.DUP(),
                    JavaOpcodes.ICONST_0(),
                )

        function = self.context.add_function(
            name=func_name,
            code=self.code_objects[(node.lineno, getattr(node, 'name', '<lambda>'))],
            parameter_signatures=parameter_signatures,
            return_signature=return_signature,
        )

        for decorator in decorator_list[::-1]:
            if func_name == '__init__' and is_call(decorator, 'super'):
                # We can ignore the @super decorator on __init__ methods.
                pass
            elif isinstance(decorator, ast.Name) and decorator.id == "classmethod":
                pass
            elif isinstance(decorator, ast.Name) and decorator.id == "staticmethod":
                pass
            else:
                self.context.add_opcodes(
                    JavaOpcodes.AASTORE(),
                    JavaOpcodes.ACONST_NULL(),
                    python.Callable.invoke(),
                )

        # Store the callable object as an accessible symbol.
        self.context.store_name(func_name)

        # Free all the variables used for default storage.
        for default in default_vars:
            self.context.add_opcodes(
                free_name(default)
            )

        return function

    @node_visitor
    def visit_Lambda(self, node):
        lambda_name = 'lambda-%x' % id(node)
        function = self._create_function(node, lambda_name, [])

        self.push_context(function)

        LocalsVisitor(function).visit(node)

        self.visit(node.body)
        self.context.add_opcodes(JavaOpcodes.ARETURN())
        self.context.opcodes[-1].needs_implicit_return = \
            self.context.has_nested_structure

        self.pop_context()

        self.context.load_name(lambda_name)

    @node_visitor
    def visit_IfExp(self, node):
        self.visit(node.test)

        self.context.add_opcodes(
            IF([python.Object.as_boolean()], JavaOpcodes.IFEQ),
        )

        self.visit(node.body)

        self.context.add_opcodes(
            ELSE(),
        )

        self.visit(node.orelse)

        self.context.add_opcodes(
            END_IF(),
        )

    @node_visitor
    def visit_Dict(self, node):
        self.context.add_opcodes(
            python.Dict()
        )

        for kchild, vchild in zip(node.keys, node.values):
            self.context.add_opcodes(
                JavaOpcodes.DUP(),
            )

            self.visit(kchild)
            self.visit(vchild)

            self.context.add_opcodes(
                python.Dict.set_item(),
            )

        self.context.add_opcodes(
        )

    @node_visitor
    def visit_Set(self, node):
        self.context.add_opcodes(
            python.Set()
        )

        for child in node.elts:
            self.context.add_opcodes(
                JavaOpcodes.DUP(),
            )

            self.visit(child)

            self.context.add_opcodes(
                python.Set.add()
            )

    @node_visitor
    def visit_ListComp(self, node):
        listcomp_name = 'listcomp_%x' % id(node)
        listcomp = self.context.add_function(
            name=listcomp_name,
            code=self.code_objects[(node.lineno, '<listcomp>')],
            parameter_signatures=[
                {
                    'name': '.%s' % i,
                    # 'annotation': name_visitor.evaluate(arg.annotation).annotation,
                    'kind': ArgType.POSITIONAL_OR_KEYWORD,
                    'default': None
                }
                for i, arg in enumerate(node.generators)
            ],
            return_signature={
                'annotation': 'org/python/types/List'
            }
        )

        # Store the callable object as an accessible symbol.
        self.context.store_name(listcomp_name)

        self.push_context(listcomp)

        LocalsVisitor(listcomp).visit(node)

        self.context.add_opcodes(
            python.List(),
        )
        self.context.store_name('#listcomp-result-%x' % id(node), declare=True)

        if len(node.generators) != 1:
            raise NotImplementedError("Don't know how to handle multiple generators")

        for i, generator in enumerate(node.generators):
            if isinstance(generator, ast.comprehension):
                self.context.add_opcodes(
                    ALOAD_name('.%s' % i),
                    python.Object.iter(),
                )
            else:
                raise NotImplementedError("Don't know how to handle generator of type %s" % type(generator))

        loop = START_LOOP()

        self.context.store_name('#listcomp-iter-%x' % id(node), declare=True)
        self.context.add_opcodes(
            loop,
        )
        self.context.add_opcodes(
                TRY(),
        )
        self.context.load_name('#listcomp-iter-%x' % id(node))
        self.context.add_opcodes(
                    python.Iterable.next(),
        )
        self.context.add_opcodes(
                CATCH('org/python/exceptions/StopIteration'),
        )
        self.context.add_opcodes(
                    JavaOpcodes.POP(),
                    jump(JavaOpcodes.GOTO(0), self.context, loop, OpcodePosition.NEXT),
        )
        self.context.add_opcodes(
                END_TRY(),
        )

        for i, generator in enumerate(node.generators):
            if isinstance(generator, ast.comprehension):
                self.visit(generator.target)

        if node.generators[0].ifs:
            self.visit(
                ast.BoolOp(ast.And(), node.generators[0].ifs)
            )

            self.context.add_opcodes(
                IF([python.Object.as_boolean()], JavaOpcodes.IFEQ),
            )

        self.visit(node.elt)

        # And add it to the result list
        self.context.load_name('#listcomp-result-%x' % id(node)),
        self.context.add_opcodes(
                JavaOpcodes.CHECKCAST('org/python/types/List'),
                JavaOpcodes.SWAP(),
                python.List.append(),
        )

        if node.generators[0].ifs:
            self.context.add_opcodes(
                END_IF()
            )

        self.context.add_opcodes(
            END_LOOP(),
        )
        self.context.load_name('#listcomp-result-%x' % id(node)),
        self.context.add_opcodes(
            JavaOpcodes.ARETURN(),
        )

        # Clean up
        self.context.delete_name('#listcomp-iter-%x' % id(node))
        self.context.delete_name('#listcomp-result-%x' % id(node))

        self.pop_context()

        # Now invoke the list comprehension
        self.context.load_name('listcomp_%x' % id(node))
        self.context.add_opcodes(
            java.Array(len(node.generators))
        )

        for i, generator in enumerate(node.generators):
            if isinstance(generator, ast.comprehension):
                self.context.add_opcodes(
                    JavaOpcodes.DUP(),
                    ICONST_val(i),
                )

                self.visit(generator.iter)

                self.context.add_opcodes(
                    JavaOpcodes.AASTORE(),
                )

        self.context.add_opcodes(
            # No keyword arguments
            JavaOpcodes.ACONST_NULL(),

            # Now invoke.
            python.Callable.invoke(),
        )

        # FIXME: This would be a much more efficient way to invoke
        # the comprehension method, but when it's a closure, it's
        # not that simple.
        # for i, generator in enumerate(node.generators):
        #     if isinstance(generator, ast.comprehension):
        #         self.visit(generator.iter)
        #
        # self.context.add_opcodes(
        #     JavaOpcodes.INVOKESTATIC(
        #         self.context.class_descriptor,
        #         'listcomp_%x' % id(node),
        #         '(%s)Lorg/python/Object;' % ''.join(
        #             'Lorg/python/Object;'
        #             for gen in node.generators
        #         )
        #     )
        # )

    @node_visitor
    def visit_SetComp(self, node):
        # Get the code object for the list comprehension.
        setcomp_name = 'setcomp_%x' % id(node)
        setcomp = self.context.add_function(
            name=setcomp_name,
            code=self.code_objects[(node.lineno, '<setcomp>')],
            parameter_signatures=[
                {
                    'name': '.%s' % i,
                    # 'annotation': name_visitor.evaluate(arg.annotation).annotation,
                    'kind': ArgType.POSITIONAL_OR_KEYWORD,
                    'default': None
                }
                for i, arg in enumerate(node.generators)
            ],
            return_signature={
                'annotation': 'org/python/types/Set'
            }
        )
        # Store the callable object as an accessible symbol.
        self.context.store_name(setcomp_name)

        self.push_context(setcomp)

        LocalsVisitor(setcomp).visit(node)

        self.context.add_opcodes(
            python.Set(),
        )
        self.context.store_name('#setcomp-result-%x' % id(node), declare=True)

        if len(node.generators) != 1:
            raise NotImplementedError("Don't know how to handle multiple generators")

        for i, generator in enumerate(node.generators):
            if isinstance(generator, ast.comprehension):
                self.context.add_opcodes(
                    ALOAD_name('.%s' % i),
                    python.Object.iter()
                )
            else:
                raise NotImplementedError("Don't know how to handle generator of type %s" % type(generator))

        self.context.store_name('#setcomp-iter-%x' % id(node), declare=True)

        loop = START_LOOP()
        self.context.add_opcodes(
            loop,
        )
        self.context.add_opcodes(
                TRY(),
        )
        self.context.load_name('#setcomp-iter-%x' % id(node))
        self.context.add_opcodes(
                    python.Iterable.next(),
        )
        self.context.add_opcodes(
                CATCH('org/python/exceptions/StopIteration'),
        )
        self.context.add_opcodes(
                    JavaOpcodes.POP(),
                    jump(JavaOpcodes.GOTO(0), self.context, loop, OpcodePosition.NEXT),
        )
        self.context.add_opcodes(
                END_TRY(),
        )

        for i, generator in enumerate(node.generators):
            if isinstance(generator, ast.comprehension):
                self.visit(generator.target)

        self.visit(node.elt)

        # And add it to the result set
        self.context.load_name('#setcomp-result-%x' % id(node))
        self.context.add_opcodes(
                JavaOpcodes.CHECKCAST('org/python/types/Set'),
                JavaOpcodes.SWAP(),
                python.Set.add(),
        )
        self.context.add_opcodes(
            END_LOOP(),
        )
        self.context.load_name('#setcomp-result-%x' % id(node)),
        self.context.add_opcodes(
            JavaOpcodes.ARETURN(),
        )

        # Clean up
        self.context.delete_name('#setcomp-iter-%x' % id(node))
        self.context.delete_name('#setcomp-result-%x' % id(node))

        self.pop_context()

        # Now invoke the set comprehension
        self.context.load_name('setcomp_%x' % id(node))
        self.context.add_opcodes(
            java.Array(len(node.generators)),
        )

        for i, generator in enumerate(node.generators):
            if isinstance(generator, ast.comprehension):
                self.context.add_opcodes(
                    JavaOpcodes.DUP(),
                    ICONST_val(i),
                )

                self.visit(generator.iter)

                self.context.add_opcodes(
                    JavaOpcodes.AASTORE(),
                )

        self.context.add_opcodes(
            # No keyword arguments
            JavaOpcodes.ACONST_NULL(),

            # Now invoke.
            python.Callable.invoke(),
        )

    @node_visitor
    def visit_DictComp(self, node):
        dictcomp_name = 'dictcomp_%x' % id(node)
        dictcomp = self.context.add_function(
            name=dictcomp_name,
            code=self.code_objects[(node.lineno, '<dictcomp>')],
            parameter_signatures=[
                {
                    'name': '.%s' % i,
                    # 'annotation': name_visitor.evaluate(arg.annotation).annotation,
                    'kind': ArgType.POSITIONAL_OR_KEYWORD,
                    'default': None
                }
                for i, arg in enumerate(node.generators)
            ],
            return_signature={
                'annotation': 'org/python/types/Dict'
            }
        )
        # Store the callable object as an accessible symbol.
        self.context.store_name(dictcomp_name)

        self.push_context(dictcomp)

        LocalsVisitor(dictcomp).visit(node)

        self.context.add_opcodes(
            java.New('org/python/types/Dict'),
            java.Init('org/python/types/Dict'),
        )
        self.context.store_name('#dictcomp-result-%x' % id(node), declare=True)

        if len(node.generators) != 1:
            raise NotImplementedError("Don't know how to handle multiple generators")

        for i, generator in enumerate(node.generators):
            if isinstance(generator, ast.comprehension):
                self.context.add_opcodes(
                    ALOAD_name('.%s' % i),
                    python.Object.iter()
                )
            else:
                raise NotImplementedError("Don't know how to handle generator of type %s" % type(generator))

        self.context.store_name('#dictcomp-iter-%x' % id(node), declare=True)

        loop = START_LOOP()
        self.context.add_opcodes(
            loop,
        )
        self.context.add_opcodes(
                TRY(),
        )
        self.context.load_name('#dictcomp-iter-%x' % id(node)),
        self.context.add_opcodes(
                    python.Iterable.next(),
        )
        self.context.add_opcodes(
                CATCH('org/python/exceptions/StopIteration'),
        )
        self.context.add_opcodes(
                    JavaOpcodes.POP(),
                    jump(JavaOpcodes.GOTO(0), self.context, loop, OpcodePosition.NEXT),
        )
        self.context.add_opcodes(
                END_TRY(),
        )

        for i, generator in enumerate(node.generators):
            if isinstance(generator, ast.comprehension):
                self.visit(generator.target)

        self.visit(node.key)
        self.context.add_opcodes(
            ASTORE_name('#dictcomp-key-%x' % id(node)),
        )

        self.visit(node.value)
        self.context.add_opcodes(
            ASTORE_name('#dictcomp-value-%x' % id(node)),
        )

        # And add it to the result list
        self.context.load_name('#dictcomp-result-%x' % id(node))
        self.context.add_opcodes(
            JavaOpcodes.CHECKCAST('org/python/types/Dict'),
            ALOAD_name('#dictcomp-key-%x' % id(node)),
            ALOAD_name('#dictcomp-value-%x' % id(node)),
            python.Dict.set_item(),
            END_LOOP(),
        )
        self.context.load_name('#dictcomp-result-%x' % id(node))
        self.context.add_opcodes(
            JavaOpcodes.ARETURN(),

            # Clean up
            free_name('#dictcomp-key-%x' % id(node)),
            free_name('#dictcomp-value-%x' % id(node))
        )

        self.context.delete_name('#dictcomp-iter-%x' % id(node))
        self.context.delete_name('#dictcomp-result-%x' % id(node))

        self.pop_context()

        # Now invoke the dict comprehension
        self.context.load_name('dictcomp_%x' % id(node))
        self.context.add_opcodes(
            java.Array(len(node.generators)),
        )

        for i, generator in enumerate(node.generators):
            if isinstance(generator, ast.comprehension):
                self.context.add_opcodes(
                    JavaOpcodes.DUP(),
                    ICONST_val(i),
                )

                self.visit(generator.iter)

                self.context.add_opcodes(
                    JavaOpcodes.AASTORE(),
                )

        self.context.add_opcodes(
            # No keyword arguments
            JavaOpcodes.ACONST_NULL(),

            # Now invoke.
            python.Callable.invoke(),
        )

    @node_visitor
    def visit_GeneratorExp(self, node):
        genexp_name = 'genexp_%x' % id(node)
        genexp = self.context.add_function(
            name=genexp_name,
            code=self.code_objects[(node.lineno, '<genexpr>')],
            parameter_signatures=[
                {
                    'name': '.%s' % i,
                    # 'annotation': name_visitor.evaluate(arg.annotation).annotation,
                    'kind': ArgType.POSITIONAL_OR_KEYWORD,
                    'default': None
                }
                for i, arg in enumerate(node.generators)
            ],
            return_signature={
                'annotation': 'org/python/types/List'
            }
        )

        # Store the callable object as an accessible symbol.
        self.context.store_name(genexp_name)

        self.push_context(genexp)

        LocalsVisitor(genexp).visit(node)

        if len(node.generators) != 1:
            raise NotImplementedError("Don't know how to handle multiple generators")

        for i, generator in enumerate(node.generators):
            if isinstance(generator, ast.comprehension):
                self.context.add_opcodes(
                    ALOAD_name('.%s' % i),
                    python.Object.iter()
                )
            else:
                raise NotImplementedError("Don't know how to handle generator of type %s" % type(generator))

        self.context.store_name('#genexp-iter-%x' % id(node), declare=True)
        loop = START_LOOP()
        self.context.add_opcodes(
            loop,
        )
        self.context.add_opcodes(
                TRY(),
        )
        self.context.load_name('#genexp-iter-%x' % id(node))
        self.context.add_opcodes(
                    python.Iterable.next(),
        )
        self.context.add_opcodes(
                CATCH('org/python/exceptions/StopIteration'),
        )
        self.context.add_opcodes(
                    JavaOpcodes.POP(),
                    jump(JavaOpcodes.GOTO(0), self.context, loop, OpcodePosition.NEXT),
        )
        self.context.add_opcodes(
                END_TRY(),
        )

        for i, generator in enumerate(node.generators):
            if isinstance(generator, ast.comprehension):
                self.visit(generator.target)

        self.visit(node.elt)

        yield_point = len(self.context.yield_points) + 1
        self.context.add_opcodes(
            # Convert to a new value for return purposes
            JavaOpcodes.INVOKEINTERFACE('org/python/Object', 'byValue', args=[], returns='Lorg/python/Object;'),

            # Save the current stack and yield index
            ALOAD_name('<generator>'),
            ALOAD_name('#locals'),
            java.Yield(yield_point),
        )

        # On restore, the next instruction is the target
        # for the restore jump.
        self.context.yield_points.append(node)
        self.context.next_resolve_list.append((node, OpcodePosition.YIELD))

        #  First thing to do is restore the state of the stack.
        self.context.add_opcodes(
            ALOAD_name('<generator>'),
            JavaOpcodes.GETFIELD('org/python/types/Generator', 'stack', 'Ljava/util/Map;'),
            ASTORE_name('#locals'),
        )

        for var, index in self.context.local_vars.items():
            if index is not None and var not in ('<generator>', '#locals'):
                self.context.add_opcodes(
                    ALOAD_name('#locals'),
                    java.Map.get(var),
                    JavaOpcodes.ASTORE(index),
                )

        self.context.add_opcodes(
            END_LOOP(),
        )

        # Clean up
        self.context.delete_name('#genexp-iter-%x' % id(node))

        self.pop_context()

        # Now invoke the list comprehension
        self.context.load_name('genexp_%x' % id(node))
        self.context.add_opcodes(
            java.Array(len(node.generators)),
        )

        for i, generator in enumerate(node.generators):
            if isinstance(generator, ast.comprehension):
                self.context.add_opcodes(
                    JavaOpcodes.DUP(),
                    ICONST_val(i),
                )

                self.visit(generator.iter)

                self.context.add_opcodes(
                    JavaOpcodes.AASTORE(),
                )

        self.context.add_opcodes(
            # No keyword arguments
            JavaOpcodes.ACONST_NULL(),

            # Now invoke.
            python.Callable.invoke(),
        )

    @node_visitor
    def visit_Yield(self, node):
        self.visit(node.value)
        yield_point = len(self.context.yield_points) + 1
        self.context.add_opcodes(
            # Convert to a new value for return purposes
            JavaOpcodes.INVOKEINTERFACE('org/python/Object', 'byValue', args=[], returns='Lorg/python/Object;')
        )
        # Save the current stack and yield inde
        self.context.load_name('<generator>')
        self.context.add_opcodes(
            ALOAD_name('#locals'),
            java.Yield(yield_point),
        )

        # On restore, the next instruction is the target
        # for the restore jump.
        self.context.yield_points.append(node)
        self.context.next_resolve_list.append((node, OpcodePosition.YIELD))

        #  First thing to do is restore the state of the stack.
        self.context.load_name('<generator>')
        self.context.add_opcodes(
            JavaOpcodes.GETFIELD('org/python/types/Generator', 'stack', 'Ljava/util/Map;'),
            ASTORE_name('#locals'),
        )

        for var, index in self.context.local_vars.items():
            if index is not None and var not in ('<generator>', '#locals'):
                self.context.add_opcodes(
                    ALOAD_name('#locals'),
                    java.Map.get(var),
                    JavaOpcodes.ASTORE(index),
                )

    @node_visitor
    def visit_YieldFrom(self, node):
        # expr value):
        raise NotImplementedError('No handler for YieldFrom')

    @node_visitor
    def visit_Compare(self, node):

        def compare_to(arg):
            if isinstance(arg, ast.Is) and not const_comparison:
                self.context.add_opcodes(
                    IF([], JavaOpcodes.IF_ACMPNE),
                )
                self.context.add_opcodes(
                        java.New('org/python/types/Bool'),
                        JavaOpcodes.ICONST_1(),
                        java.Init('org/python/types/Bool', 'Z'),
                )
                self.context.add_opcodes(
                    ELSE(),
                )
                self.context.add_opcodes(
                        java.New('org/python/types/Bool'),
                        JavaOpcodes.ICONST_0(),
                        java.Init('org/python/types/Bool', 'Z'),
                )
                self.context.add_opcodes(
                    END_IF(),
                )

            elif isinstance(arg, ast.IsNot) and not const_comparison:
                self.context.add_opcodes(
                    IF([], JavaOpcodes.IF_ACMPEQ),
                )
                self.context.add_opcodes(
                        java.New('org/python/types/Bool'),
                        JavaOpcodes.ICONST_1(),
                        java.Init('org/python/types/Bool', 'Z'),
                )
                self.context.add_opcodes(
                    ELSE(),
                )
                self.context.add_opcodes(
                        java.New('org/python/types/Bool'),
                        JavaOpcodes.ICONST_0(),
                        java.Init('org/python/types/Bool', 'Z'),
                )
                self.context.add_opcodes(
                    END_IF(),
                )

            else:
                if isinstance(arg, (ast.In, ast.NotIn)):
                    self.context.add_opcodes(
                        JavaOpcodes.SWAP()
                    )

                oper = {
                        ast.Eq: '__eq__',
                        ast.Gt: '__gt__',
                        ast.GtE: '__ge__',
                        ast.Lt: '__lt__',
                        ast.LtE: '__le__',
                        ast.In: '__contains__',
                        ast.Is: '__eq__',
                        ast.IsNot: '__ne__',
                        ast.NotEq: '__ne__',
                        ast.NotIn: '__not_contains__',
                }[type(arg)]
                oper_symbol = {
                        ast.Eq: '==',
                        ast.Gt: '>',
                        ast.GtE: '>=',
                        ast.Lt: '<',
                        ast.LtE: '<=',
                        ast.In: 'in',
                        ast.Is: 'is',
                        ast.IsNot: 'is not',
                        ast.NotEq: '!=',
                        ast.NotIn: 'not in',
                }[type(arg)]
                reflect_oper = {
                        ast.Eq: '__eq__',
                        ast.Gt: '__lt__',
                        ast.GtE: '__le__',
                        ast.Lt: '__gt__',
                        ast.LtE: '__ge__',
                        ast.In: '__contains__',
                        ast.Is: '__eq__',
                        ast.IsNot: '__ne__',
                        ast.NotEq: '__ne__',
                        ast.NotIn: '__not_contains__',
                }[type(arg)]

                self.context.add_opcodes(
                    JavaOpcodes.LDC_W(oper_symbol),
                    JavaOpcodes.LDC_W(oper),
                    JavaOpcodes.LDC_W(reflect_oper),
                    JavaOpcodes.INVOKESTATIC(
                        'org/python/types/Object',
                        '__cmp__',
                        args=[
                            'Lorg/python/Object;',
                            'Lorg/python/Object;',
                            'Ljava/lang/String;',
                            'Ljava/lang/String;',
                            'Ljava/lang/String;',
                        ],
                        returns='Lorg/python/Object;',
                    ),
                )

        self.visit(node.left)
        left = node.left

        for i, (operation, right) in enumerate(zip(node.ops, node.comparators)):
            self.visit(right)
            const_comparison = isinstance(left, ast.Num) | isinstance(right, ast.Num)
            if i < len(node.ops) - 1:
                self.context.add_opcodes(
                        JavaOpcodes.DUP_X1()
                        )
                compare_to(operation)
                self.context.add_opcodes(
                    JavaOpcodes.DUP()
                )
                self.context.add_opcodes(
                    IF([python.Object.as_boolean()], JavaOpcodes.IFNE)
                )
                self.context.add_opcodes(
                        JavaOpcodes.SWAP(),
                        JavaOpcodes.POP()
                )
                self.context.add_opcodes(
                    ELSE()
                )
                self.context.add_opcodes(
                        JavaOpcodes.POP()
                )
            else:
                compare_to(operation)
            left = right

        for _ in range(len(node.ops) - 1):
            self.context.add_opcodes(
                END_IF()
            )

    @node_visitor
    def visit_Call(self, node):
        if is_call(node, ('locals', 'globals', 'vars')):
            # **kwargs is node.keywords[None] in Python 3.5; node.kwargs in earlier versions
            if None in node.keywords or getattr(node, 'kwargs', None):
                self.context.add_opcodes(
                    java.New('org/python/exceptions/TypeError'),
                    JavaOpcodes.LDC_W(node.func.id + "() takes no keyword arguments"),
                    java.Init('org/python/exceptions/TypeError', 'Ljava/lang/String;'),
                    JavaOpcodes.ATHROW()
                )
            elif node.args:
                self.context.add_opcodes(
                    java.New('org/python/exceptions/TypeError'),
                    JavaOpcodes.LDC_W(node.func.id + "() takes no arguments (" + len(node.args) + " given)"),
                    java.Init('org/python/exceptions/TypeError', 'Ljava/lang/String;'),
                    JavaOpcodes.ATHROW()
                )
            else:
                # Create a dict for storage
                self.context.add_opcodes(
                    java.New('org/python/types/Dict'),
                    java.New('org/python/internals/Scope'),
                )

                getattr(self.context, 'load_%s' % node.func.id)()

                self.context.add_opcodes(
                    # Wrap the locals/globals/vars to make them look like a Python String->Object map
                    java.Init('org/python/internals/Scope', 'Ljava/util/Map;'),
                    # Construct a dictionary based on that map
                    java.Init('org/python/types/Dict', 'Ljava/util/Map;'),
                )

        elif is_call(node, 'super'):
            # context.add_opcodes(
            #     DEBUG("ATTRIBUTE ON SUPER"),
            # )

            if len(node.args) == 0:
                self.context.add_opcodes(
                    java.New('org/python/types/Super'),

                    # The super class to bind to.
                    python.Type.for_name(self.context.klass.descriptor),

                    # Bind to self. Since we know we are in a class building context,
                    # we can be certain that register 0 contains self.
                    JavaOpcodes.ALOAD_0(),
                    java.Init('org/python/types/Super', 'Lorg/python/Object;', 'Lorg/python/Object;'),
                )

            elif len(node.args) == 1:  # Unbound super
                # FIXME: This is an unusual call pattern for super(), so it
                # isn't obvious what the right behavior should be...
                self.context.add_opcodes(
                    java.New('org/python/types/Super'),
                )

                # The super class to bind to.
                self.visit(node.args[0])

                self.context.add_opcodes(
                    java.Init('org/python/types/Super', 'Lorg/python/Object;'),
                )

            elif len(node.args) == 2:  # Bound super
                self.context.add_opcodes(
                    java.New('org/python/types/Super'),
                )

                # The super class to bind to.
                self.visit(node.args[0])

                # The instance to bind to.
                self.visit(node.args[1])

                self.context.add_opcodes(
                    java.Init('org/python/types/Super', 'Lorg/python/Object;', 'Lorg/python/Object;'),
                )

            else:
                raise Exception("Invalid number of arguments to super()")

        else:
            # Evaluate the callable, and check that it *is* a callable
            self.visit(node.func)

            self.context.add_opcodes(
                JavaOpcodes.CHECKCAST('org/python/Callable'),
            )

            # Create and populate the array of arguments to pass to invoke()
            num_args = len([arg for arg in node.args if not isinstance(arg, ast.Starred)])

            self.context.add_opcodes(
                java.Array(num_args),
            )

            for i, arg in enumerate(node.args):
                # This block implements *args in Python 3.5+
                if isinstance(arg, ast.Starred):
                    self.visit(arg)
                    continue

                self.context.add_opcodes(
                    JavaOpcodes.DUP(),
                    ICONST_val(i),
                )
                self.visit(arg)
                self.context.add_opcodes(
                    JavaOpcodes.AASTORE(),
                )

            # This block implements *args in Python 3.4
            if getattr(node, 'starargs', None) is not None:
                # Evaluate the starargs
                self.visit(node.starargs)

                self.context.add_opcodes(
                    AddToArgs(),
                )

            # Create and populate the map of kwargs to pass to invoke().
            self.context.add_opcodes(
                    java.Map(),
            )

            for keyword in node.keywords:
                if keyword.arg is None:  # Python 3.5 **kwargs
                    self.add_doublestarred_kwargs(node, keyword.value)
                    continue

                self.context.add_opcodes(
                    JavaOpcodes.DUP(),
                    JavaOpcodes.LDC_W(keyword.arg),
                )
                self.visit(keyword.value)
                self.context.add_opcodes(
                    java.Map.put()
                )

            if getattr(node, 'kwargs', None) is not None:  # Python 3.4 **kwargs
                self.add_doublestarred_kwargs(node, node.kwargs)

            # Set up the stack and invoke the callable
            self.context.add_opcodes(
                python.Callable.invoke(),
            )

    @node_visitor
    def visit_Starred(self, node):
        # Handle *args at a call site (Python 3.5+)
        # Evaluate the starargs
        self.visit(node.value)

        self.context.add_opcodes(
            AddToArgs(),
        )

    def add_doublestarred_kwargs(self, node, kwargs):
        self.visit(kwargs)

        # Add all the kwargs to the kwargs dict.
        try:
            func_name = node.func.id
        except AttributeError:
            func_name = node.func.attr

        self.context.add_opcodes(
            AddToKwargs(func_name)
        )

    @node_visitor
    def visit_Num(self, node):
        if isinstance(node.n, int):
            self.context.add_int(node.n)
        elif isinstance(node.n, float):
            self.context.add_float(node.n)
        elif isinstance(node.n, complex):
            self.context.add_complex(node.n)
        else:
            raise NotImplementedError('Unknown number type %s' % type(node.n))

    @node_visitor
    def visit_Str(self, node):
        self.context.add_str(node.s)

    @node_visitor
    def visit_Bytes(self, node):
        self.context.add_opcodes(
            java.New('org/python/types/Bytes'),

            JavaOpcodes.BIPUSH(len(node.s)),
            JavaOpcodes.NEWARRAY(JavaOpcodes.NEWARRAY.T_BYTE),
        )

        for i, b in enumerate(node.s):
            self.context.add_opcodes(
                JavaOpcodes.DUP(),
                ICONST_val(i),
                JavaOpcodes.BIPUSH(node.s[i]),
                JavaOpcodes.BASTORE(),
            )

        self.context.add_opcodes(
            java.Init('org/python/types/Bytes', '[B')
        )

    @node_visitor
    def visit_NameConstant(self, node):
        if node.value is None:
            self.context.add_opcodes(
                python.NONE()
            )
        elif node.value is True:
            self.context.add_opcodes(
                java.New('org/python/types/Bool'),
                JavaOpcodes.ICONST_1(),
                java.Init('org/python/types/Bool', 'Z'),
            )
        elif node.value is False:
            self.context.add_opcodes(
                java.New('org/python/types/Bool'),
                JavaOpcodes.ICONST_0(),
                java.Init('org/python/types/Bool', 'Z'),
            )
        else:
            raise NotImplementedError("Unknown named constant %s" % node.value)

    @node_visitor
    def visit_Ellipsis(self, node):
        raise NotImplementedError('No handler for Ellipsis')

    @node_visitor
    def visit_Attribute(self, node, ctx=None):
        ctx = ctx or node.ctx
        self.visit(node.value)

        if type(ctx) == ast.Load:
            self.context.add_opcodes(
                python.Object.get_attribute(node.attr),
            )
        elif type(ctx) == ast.Store:
            self.context.add_opcodes(
                JavaOpcodes.SWAP(),
                python.Object.set_attr(node.attr),
            )
        elif type(ctx) == ast.Del:
            self.context.add_opcodes(
                JavaOpcodes.LDC_W(node.attr),
            )
        else:
            raise NotImplementedError("Unknown context %s" % ctx)

    @node_visitor
    def visit_Subscript(self, node, ctx=None):
        ctx = ctx or node.ctx
        if type(ctx) == ast.Load:
            self.visit(node.value)
            self.visit(node.slice)
            self.context.add_opcodes(
                python.Object.get_item()
            )
        elif type(ctx) == ast.Store:
            self.context.add_opcodes(
                ASTORE_name('#value'),
            )
            self.visit(node.value)
            self.visit(node.slice)
            self.context.add_opcodes(
                ALOAD_name('#value'),
                python.Object.set_item(),
                free_name('#value'),
            )
        elif type(ctx) == ast.Del:
            self.visit(node.value)
            self.visit(node.slice)
        else:
            raise NotImplementedError("Unknown context %s" % node.ctx)

    @node_visitor
    def visit_Name(self, node):
        if type(node.ctx) == ast.Load:
            try:
                self.context.load_name(node.id)
            except NameError:
                self.context.add_opcodes(
                    java.New('org/python/exceptions/UnboundLocalError'),
                    JavaOpcodes.LDC_W(node.id),
                    java.Init('org/python/exceptions/UnboundLocalError', 'Ljava/lang/String;'),
                    JavaOpcodes.ATHROW()
                )
        elif type(node.ctx) == ast.Store:
            self.context.store_name(node.id)
        elif type(node.ctx) == ast.Del:
            self.context.delete_name(node.id)
        else:
            raise NotImplementedError("Unknown context %s" % node.ctx)

    @node_visitor
    def visit_List(self, node):
        if isinstance(node.ctx, ast.Load):
            self.context.add_opcodes(
                python.List()
            )

            for child in node.elts:
                self.context.add_opcodes(
                    JavaOpcodes.DUP(),
                )

                self.visit(child)

                self.context.add_opcodes(
                    python.List.append()
                )

        elif isinstance(node.ctx, ast.Store):
            self.context.add_opcodes(
                python.Object.iter()
            )
            for child in node.elts:
                self.context.add_opcodes(
                    JavaOpcodes.DUP(),
                    python.Iterable.next()
                )
                self.visit(child)

    @node_visitor
    def visit_Tuple(self, node):
        if isinstance(node.ctx, ast.Load):
            self.context.add_opcodes(
                java.New('org/python/types/Tuple'),

                java.List(len(node.elts))
            )

            for child in node.elts:
                self.context.add_opcodes(
                    JavaOpcodes.DUP(),
                )

                self.visit(child)

                self.context.add_opcodes(
                    java.List.add()
                )

            self.context.add_opcodes(
                java.Init('org/python/types/Tuple', 'Ljava/util/List;')
            )

        elif isinstance(node.ctx, ast.Store):
            self.context.add_opcodes(
                python.Object.iter()
            )
            for child in node.elts:
                self.context.add_opcodes(
                    JavaOpcodes.DUP(),
                    python.Iterable.next()
                )
                self.visit(child)
            self.context.add_opcodes(
                JavaOpcodes.POP(),
            )

    @node_visitor
    def visit_Slice(self, node):
        self.context.add_opcodes(
            java.New('org/python/types/Slice'),
        )
        if node.lower:
            self.visit(node.lower)
        else:
            self.context.add_opcodes(
                python.NONE()
            )

        if node.upper:
            self.visit(node.upper)
        else:
            self.context.add_opcodes(
                python.NONE()
            )

        if node.step:
            self.visit(node.step)
        else:
            self.context.add_opcodes(
                python.NONE()
            )

        self.context.add_opcodes(
            java.Init('org/python/types/Slice', 'Lorg/python/Object;', 'Lorg/python/Object;', 'Lorg/python/Object;')
        )

    @node_visitor
    def visit_ExtSlice(self, node):
        # slice* dims):
        raise NotImplementedError('No handler for ExtSlice')

    @node_visitor
    def visit_Index(self, node):
        self.visit(node.value)

    @node_visitor
    def visit_ExceptHandler(self, node):
        # expr? type, identifier? name, stmt* body):
        if isinstance(node.type, ast.Tuple):
            exception = [
                self.full_classref(exc.id, default_prefix='org.python.exceptions')
                for exc in node.type.elts
            ]
        elif node.type:
            exception = self.full_classref(node.type.id, default_prefix='org.python.exceptions')
        else:
            exception = None

        self.context.add_opcodes(
            CATCH(exception),
        )

        # Top of stack is the exception to be raised
        if exception and node.name:
            # The exception has been named. Store it as that name.
            self.context.add_opcodes(
                JavaOpcodes.DUP(),
            )
            self.context.store_name(node.name)

        # Regardless of whether the exception is named,
        # locally store it so that it can be re-raised easily.
        exc_name = '#exception-%x' % id(node)
        self.context.add_opcodes(
            ASTORE_name(exc_name),
        )

        self.current_exc_name.append(exc_name)

        for child in node.body:
            self.visit(child)

        self.context.add_opcodes(
            free_name(exc_name)
        )
        self.current_exc_name.pop()
