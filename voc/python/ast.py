import ast
import sys

from ..java import opcodes as JavaOpcodes
from .modules import Module, ModuleBlock
from .methods import Method, MainMethod
from .utils import (
    IF, ELSE, END_IF,
    TRY, CATCH, END_TRY,
    ICONST_val,
    jump, OpcodePosition
)


def is_mainline(node):
    return (
        # Node is an if statement...
        isinstance(node, ast.If)
        # ... doing a comparison ...
        and isinstance(node.test, ast.Compare)
        # ... that is an equality comparison ...
        and len(node.test.ops) == 1 and isinstance(node.test.ops[0], ast.Eq)
        # ... where the LHS is the symbol __name__
        and isinstance(node.test.left, ast.Name) and node.test.left.id == '__name__'
        # ... and the RHS is the string '__main__'
        and len(node.test.comparators) == 1 and isinstance(node.test.comparators[0], ast.Str)
            and node.test.comparators[0].s == '__main__'
    )


def node_visitor(fn):
    def dec(self, node):
        try:
            if node.lineno != self._current_line:
                self._current_line = self.context.next_opcode_starts_line = node.lineno
        except AttributeError:
            pass
        self.context.next_resolve_list.append((node, OpcodePosition.START))
        fn(self, node)
        self.context.next_resolve_list.append((node, OpcodePosition.END))
        self.context.next_resolve_list.append((node, OpcodePosition.NEXT))
    return dec


class Visitor(ast.NodeVisitor):
    def __init__(self, namespace, filename, verbosity=1):
        super().__init__()
        self.namespace = namespace
        self.filename = filename
        self.verbosity = verbosity

        self._current_line = None
        self._context = []
        self._root_module = None

    @property
    def context(self):
        return self._context[-1]

    def visit(self, root_node):
        super().visit(root_node)
        return self._root_module

    def visit_Module(self, node):
        module = Module(self.namespace, self.filename)
        self._context.append(module)
        if self._root_module is None:
            self._root_module = module

        main = None
        module.body = ModuleBlock(module)

        for child in node.body:
            if is_mainline(child):
                if main is not None:
                    print("Found duplicate main block... replacing previous main", file=sys.stderr)

                main = MainMethod(module)
                self._context.append(main)
                self.visit(child)
                self._context.pop()
            else:
                self._context.append(module.body)
                self.visit(child)
                self._context.pop()

        if main is None:
            if self.verbosity:
                print("Adding default main method...")
            main = MainMethod(module)

        module.methods.append(main)

        self._context.pop()

    @node_visitor
    def visit_Interactive(self, node):
        # stmt* body):
        raise NotImplementedError('No handler for Interactive')

    @node_visitor
    def visit_Expr(self, node):
        # No special handling required for Expr nodes.
        self.generic_visit(node)

    @node_visitor
    def visit_Suite(self, node):
        # stmt* body):
        raise NotImplementedError('No handler for Suite')

    # # Statements
    @node_visitor
    def visit_FunctionDef(self, node):
        # identifier name, arguments args, stmt* body, expr* decorator_list, expr? returns):
        method = self.context.add_method(node)

        self._context.append(method)
        for child in node.body:
            self.visit(child)
        self._context.pop()

    @node_visitor
    def visit_ClassDef(self, node):
        # identifier name, expr* bases, keyword* keywords, expr? starargs, expr? kwargs, stmt* body, expr* decorator_list):
        raise NotImplementedError('No handler for ClassDef')

    @node_visitor
    def visit_Return(self, node):
        # expr? value):
        raise NotImplementedError('No handler for Return')

    @node_visitor
    def visit_Delete(self, node):
        # expr* targets):
        raise NotImplementedError('No handler for Delete')

    def _set_target(self, target):
        if type(target) == ast.Attribute:
            self.visit(target.value)
            self.context.add_opcodes(
                JavaOpcodes.SWAP(),
                JavaOpcodes.LDC_W(target.attr),
                JavaOpcodes.SWAP(),
                JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__setattr__', '(Ljava/lang/String;Lorg/python/Object;)V'),
            )
        elif type(target) == ast.Name:
            self.context.store_name(target.id, use_locals=False)
        else:
            raise NotImplementedError('Unknown assignment target type %s' % type(target))

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
                self._set_target(target)
            self.context.add_opcodes(
                JavaOpcodes.POP()
            )
        else:
            self._set_target(node.targets[0])

    @node_visitor
    def visit_AugAssign(self, node):
        # expr target, operator op, expr value):
        raise NotImplementedError('No handler for AugAssign')

    @node_visitor
    def visit_For(self, node):
        # expr target, expr iter, stmt* body, stmt* orelse):
        raise NotImplementedError('No handler for For')

    @node_visitor
    def visit_While(self, node):
        # expr test, stmt* body, stmt* orelse):
        raise NotImplementedError('No handler for While')

    @node_visitor
    def visit_If(self, node):
        # expr test, stmt* body, stmt* orelse):
        self.visit(node.test)

        self.context.add_opcodes(
            IF([
                    JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__bool__', '()Lorg/python/Object;'),
                    JavaOpcodes.CHECKCAST('org/python/types/Bool'),
                    JavaOpcodes.GETFIELD('org/python/types/Bool', 'value', 'Z'),
                ], JavaOpcodes.IFEQ),
        )

        for child in node.body:
            self.visit(child)

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
        raise NotImplementedError('No handler for With')

    @node_visitor
    def visit_Raise(self, node):
        # expr? exc, expr? cause):
        raise NotImplementedError('No handler for Raise')

    @node_visitor
    def visit_Try(self, node):
        # stmt* body, excepthandler* handlers, stmt* orelse, stmt* finalbody):
        raise NotImplementedError('No handler for Try')

    @node_visitor
    def visit_Assert(self, node):
        # expr test, expr? msg):
        raise NotImplementedError('No handler for Assert')

    @node_visitor
    def visit_Import(self, node):
        for alias in node.names:
            self.context.add_opcodes(
                JavaOpcodes.LDC_W(alias.name),
                JavaOpcodes.ACONST_NULL(),
                JavaOpcodes.ICONST_0(),
                JavaOpcodes.INVOKESTATIC('org/python/ImportLib', '__import__', '(Ljava/lang/String;[Ljava/lang/String;I)Lorg/python/types/Module;')
            )
            if alias.asname:
                self.context.store_name(alias.asname, use_locals=True)
            else:
                self.context.store_name(alias.name, use_locals=True)

    @node_visitor
    def visit_ImportFrom(self, node):
        self.context.add_opcodes(
            JavaOpcodes.LDC_W(node.module),

            ICONST_val(len(node.names)),
            JavaOpcodes.ANEWARRAY('java/lang/String'),
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
            JavaOpcodes.INVOKESTATIC('org/python/ImportLib', '__import__', '(Ljava/lang/String;[Ljava/lang/String;I)Lorg/python/types/Module;')
        )

        if len(node.names) == 1 and node.names[0].name == '*':
            # Find exported symbols (__all__, or everything but private "_" symbols)
            self.context.add_opcodes(
                JavaOpcodes.INVOKESTATIC('org/python/ImportLib', 'importAll', '(Lorg/python/types/Module;)Ljava/util/Map;')
            )

            # Add all the exported symbols to the currrent context
            self.context.store_dynamic()
        else:
            for alias in node.names:
                self.context.add_opcodes(
                    JavaOpcodes.DUP(),
                    JavaOpcodes.LDC_W(alias.name),
                    JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__getattribute__', '(Ljava/lang/String;)Lorg/python/Object;'),
                )

                if alias.asname:
                    self.context.store_name(alias.asname, use_locals=True)
                else:
                    self.context.store_name(alias.name, use_locals=True)

            self.context.add_opcodes(
                JavaOpcodes.POP(),
            )

    @node_visitor
    def visit_Global(self, node):
        # identifier* names):
        raise NotImplementedError('No handler for Global')

    @node_visitor
    def visit_Nonlocal(self, node):
        # identifier* names):
        raise NotImplementedError('No handler for Nonlocal')

    @node_visitor
    def visit_Pass(self, node):
    # #
    #     print("Pass", dir(node))
        raise NotImplementedError('No handler for Pass')

    @node_visitor
    def visit_Break(self, node):
    # #
    #     print("Break", dir(node))
        raise NotImplementedError('No handler for Break')

    @node_visitor
    def visit_Continue(self, node):
    # #
    #     print("Continue", dir(node))
        raise NotImplementedError('No handler for Continue')

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
                JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__bool__', '()Lorg/python/Object;'),
                JavaOpcodes.CHECKCAST('org/python/types/Bool'),
                JavaOpcodes.GETFIELD('org/python/types/Bool', 'value', 'Z'),
                jump(comparison(0), self.context, node, OpcodePosition.END),

                # This value wasn't a match; pop it off the stack.
                JavaOpcodes.POP(),
            )
        # The last value is the failsafe.
        self.visit(node.values[-1])

    @node_visitor
    def visit_BinOp(self, node):
        # expr left, operator op, expr right):
        raise NotImplementedError('No handler for BinOp')

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
                '()Lorg/python/Object;'
            )
        )

    @node_visitor
    def visit_Lambda(self, node):
        # arguments args, expr body):
        raise NotImplementedError('No handler for Lambda')

    @node_visitor
    def visit_IfExp(self, node):
        self.visit(node.test)

        self.context.add_opcodes(
            IF([
                    JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__bool__', '()Lorg/python/Object;'),
                    JavaOpcodes.CHECKCAST('org/python/types/Bool'),
                    JavaOpcodes.GETFIELD('org/python/types/Bool', 'value', 'Z'),
                ], JavaOpcodes.IFEQ),
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
            JavaOpcodes.NEW('org/python/types/Dict'),
            JavaOpcodes.DUP(),

            JavaOpcodes.NEW('java/util/HashMap'),
            JavaOpcodes.DUP(),
            JavaOpcodes.INVOKESPECIAL('java/util/HashMap', '<init>', '()V')
        )

        for kchild, vchild in zip(node.keys, node.values):
            self.context.add_opcodes(
                JavaOpcodes.DUP(),
            )

            self.visit(kchild)
            self.visit(vchild)

            self.context.add_opcodes(
                JavaOpcodes.INVOKEINTERFACE('java/util/Map', 'put', '(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;'),
                JavaOpcodes.POP(),
            )

        self.context.add_opcodes(
            JavaOpcodes.INVOKESPECIAL('org/python/types/Dict', '<init>', '(Ljava/util/Map;)V')
        )

    @node_visitor
    def visit_Set(self, node):
        self.context.add_opcodes(
            JavaOpcodes.NEW('org/python/types/Set'),
            JavaOpcodes.DUP(),

            JavaOpcodes.NEW('java/util/HashSet'),
            JavaOpcodes.DUP(),
            JavaOpcodes.INVOKESPECIAL('java/util/HashSet', '<init>', '()V')
        )

        for child in node.elts:
            self.context.add_opcodes(
                JavaOpcodes.DUP(),
            )

            self.visit(child)

            self.context.add_opcodes(
                JavaOpcodes.INVOKEINTERFACE('java/util/Set', 'add', '(Ljava/lang/Object;)Z'),
                JavaOpcodes.POP(),
            )

        self.context.add_opcodes(
            JavaOpcodes.INVOKESPECIAL('org/python/types/Set', '<init>', '(Ljava/util/Set;)V')
        )

    @node_visitor
    def visit_ListComp(self, node):
        # expr elt, comprehension* generators):
        raise NotImplementedError('No handler for ListComp')

    @node_visitor
    def visit_SetComp(self, node):
        # expr elt, comprehension* generators):
        raise NotImplementedError('No handler for SetComp')

    @node_visitor
    def visit_DictComp(self, node):
        # expr key, expr value, comprehension* generators):
        raise NotImplementedError('No handler for DictComp')

    @node_visitor
    def visit_GeneratorExp(self, node):
        # expr elt, comprehension* generators):
        raise NotImplementedError('No handler for GeneratorExp')

    @node_visitor
    def visit_Yield(self, node):
        # expr? value):
        raise NotImplementedError('No handler for Yield')

    @node_visitor
    def visit_YieldFrom(self, node):
        # expr value):
        raise NotImplementedError('No handler for YieldFrom')

    @node_visitor
    def visit_Compare(self, node):
        self.visit(node.left)
        const_comparison = type(node.left) == ast.Num

        if len(node.comparators) == 1:
            self.visit(node.comparators[0])
            const_comparison |= type(node.comparators[0]) == ast.Num
        else:
            raise NotImplementedError("Don't know how to resolve multiple comparators")

        if len(node.ops) == 1:
            if type(node.ops[0]) == ast.Is and not const_comparison:
                self.context.add_opcodes(
                    IF([], JavaOpcodes.IF_ACMPNE),
                        JavaOpcodes.NEW('org/python/types/Bool'),
                        JavaOpcodes.DUP(),
                        JavaOpcodes.ICONST_1(),
                        JavaOpcodes.INVOKESPECIAL('org/python/types/Bool', '<init>', '(Z)V'),
                    ELSE(),
                        JavaOpcodes.NEW('org/python/types/Bool'),
                        JavaOpcodes.DUP(),
                        JavaOpcodes.ICONST_0(),
                        JavaOpcodes.INVOKESPECIAL('org/python/types/Bool', '<init>', '(Z)V'),
                    END_IF(),
                )

            elif type(node.ops[0]) == ast.IsNot and not const_comparison:
                self.context.add_opcodes(
                    IF([], JavaOpcodes.IF_ACMPEQ),
                        JavaOpcodes.NEW('org/python/types/Bool'),
                        JavaOpcodes.DUP(),
                        JavaOpcodes.ICONST_1(),
                        JavaOpcodes.INVOKESPECIAL('org/python/types/Bool', '<init>', '(Z)V'),
                    ELSE(),
                        JavaOpcodes.NEW('org/python/types/Bool'),
                        JavaOpcodes.DUP(),
                        JavaOpcodes.ICONST_0(),
                        JavaOpcodes.INVOKESPECIAL('org/python/types/Bool', '<init>', '(Z)V'),
                    END_IF(),
                )

            else:
                if type(node.ops[0]) in (ast.In, ast.NotIn):
                    self.context.add_opcodes(
                        JavaOpcodes.SWAP()
                    )

                self.context.add_opcodes(
                    JavaOpcodes.INVOKEINTERFACE(
                        'org/python/Object',
                        {
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
                        }[type(node.ops[0])],
                        '(Lorg/python/Object;)Lorg/python/Object;'
                    )
                )
        else:
            raise NotImplementedError("Don't know how to resolve multiple operators")

    @node_visitor
    def visit_Call(self, node):
        # Evaluate the callable, and check that it *is* a callable
        self.visit(node.func)
        self.context.add_opcodes(
            JavaOpcodes.CHECKCAST('org/python/Callable'),
        )

        # Create and populate the array of arguments to pass to invoke()
        self.context.add_opcodes(
            ICONST_val(len(node.args)),
            JavaOpcodes.ANEWARRAY('org/python/Object'),
        )

        if node.args is not None:
            for i, arg in enumerate(node.args):
                self.context.add_opcodes(
                    JavaOpcodes.DUP(),
                    ICONST_val(i),
                )
                self.visit(arg)
                self.context.add_opcodes(
                    JavaOpcodes.AASTORE(),
                )

        # if node.starargs is not None:
        #     for arg in node.starargs:
        #         self.context.add_opcodes(
        #             JavaOpcodes.DUP(),
        #             ICONST_val(i),
        #         )
        #         self.generic_visit(arg)
        #         self.context.add_opcodes(
        #             JavaOpcodes.AASTORE(),
        #         )

        # Create and populate the map of kwargs to pass to invoke().
        self.context.add_opcodes(
            JavaOpcodes.NEW('java/util/HashMap'),
            JavaOpcodes.DUP(),
            JavaOpcodes.INVOKESPECIAL('java/util/HashMap', '<init>', '()V')
        )

        if node.keywords is not None:
            for arg, val in node.keywords:
                self.context.add_opcodes(
                    JavaOpcodes.DUP(),
                    JavaOpcodes.LDC_W(arg),
                )
                self.visit(val)
                self.context.add_opcodes(
                    JavaOpcodes.INVOKEINTERFACE('java/util/Map', 'put', '(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;'),
                    JavaOpcodes.POP()
                )

        # if node.kwargs is not None:
        #     for arg in node.kwargs:
        #         self.generic_visit(arg)

        # Set up the stack and invoke the callable
        self.context.add_opcodes(
            JavaOpcodes.INVOKEINTERFACE('org/python/Callable', 'invoke', '([Lorg/python/Object;Ljava/util/Map;)Lorg/python/Object;'),
        )

    @node_visitor
    def visit_Num(self, node):
        if isinstance(node.n, int):
            self.context.add_int(node.n)
        elif isinstance(node.n, float):
            self.context.add_float(node.n)
        else:
            raise NotImplementedError('Unknown number type %s' % type(node.n))

    @node_visitor
    def visit_Str(self, node):
        self.context.add_str(node.s)

    @node_visitor
    def visit_Bytes(self, node):
    #     bytes s):
        raise NotImplementedError('No handler for Bytes')

    @node_visitor
    def visit_NameConstant(self, node):
        if node.value is None:
            self.context.add_opcodes(
                JavaOpcodes.GETSTATIC('org/python/types/NoneType', 'NONE', 'Lorg/python/Object;')
            )
        elif node.value is True:
            self.context.add_opcodes(
                JavaOpcodes.NEW('org/python/types/Bool'),
                JavaOpcodes.DUP(),
                JavaOpcodes.ICONST_1(),
                JavaOpcodes.INVOKESPECIAL('org/python/types/Bool', '<init>', '(Z)V'),
            )
        elif node.value is False:
            self.context.add_opcodes(
                JavaOpcodes.NEW('org/python/types/Bool'),
                JavaOpcodes.DUP(),
                JavaOpcodes.ICONST_0(),
                JavaOpcodes.INVOKESPECIAL('org/python/types/Bool', '<init>', '(Z)V'),
            )
        else:
            raise NotImplementedError("Unknown named constant %s" % node.value)

    @node_visitor
    def visit_Ellipsis(self, node):
        raise NotImplementedError('No handler for Ellipsis')

    @node_visitor
    def visit_Attribute(self, node):
        self.visit(node.value)

        self.context.add_opcodes(
            JavaOpcodes.LDC_W(node.attr),
            JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__getattribute__', '(Ljava/lang/String;)Lorg/python/Object;'),
        )

    @node_visitor
    def visit_Subscript(self, node):
        self.visit(node.value)
        self.visit(node.slice)
        self.context.add_opcodes(
            JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__getitem__', '(Lorg/python/Object;)Lorg/python/Object;'),
        )

    @node_visitor
    def visit_Starred(self, node):
        # expr value, expr_context ctx):
        raise NotImplementedError('No handler for Starred')

    @node_visitor
    def visit_Name(self, node):
        self.context.load_name(node.id, use_locals=True)

    @node_visitor
    def visit_List(self, node):
        self.context.add_opcodes(
            JavaOpcodes.NEW('org/python/types/List'),
            JavaOpcodes.DUP(),

            JavaOpcodes.NEW('java/util/ArrayList'),
            JavaOpcodes.DUP(),
            ICONST_val(len(node.elts)),
            JavaOpcodes.INVOKESPECIAL('java/util/ArrayList', '<init>', '(I)V')
        )

        for child in node.elts:
            self.context.add_opcodes(
                JavaOpcodes.DUP(),
            )

            self.visit(child)

            self.context.add_opcodes(
                JavaOpcodes.INVOKEINTERFACE('java/util/List', 'add', '(Ljava/lang/Object;)Z'),
                JavaOpcodes.POP(),
            )

        self.context.add_opcodes(
            JavaOpcodes.INVOKESPECIAL('org/python/types/List', '<init>', '(Ljava/util/List;)V')
        )

    @node_visitor
    def visit_Tuple(self, node):
        self.context.add_opcodes(
            JavaOpcodes.NEW('org/python/types/Tuple'),
            JavaOpcodes.DUP(),

            JavaOpcodes.NEW('java/util/ArrayList'),
            JavaOpcodes.DUP(),
            ICONST_val(len(node.elts)),
            JavaOpcodes.INVOKESPECIAL('java/util/ArrayList', '<init>', '(I)V')
        )

        for child in node.elts:
            self.context.add_opcodes(
                JavaOpcodes.DUP(),
            )

            self.visit(child)

            self.context.add_opcodes(
                JavaOpcodes.INVOKEINTERFACE('java/util/List', 'add', '(Ljava/lang/Object;)Z'),
                JavaOpcodes.POP(),
            )

        self.context.add_opcodes(
            JavaOpcodes.INVOKESPECIAL('org/python/types/Tuple', '<init>', '(Ljava/util/List;)V')
        )

    @node_visitor
    def visit_Slice(self, node):
        # expr? lower, expr? upper, expr? step):
        self.context.add_opcodes(
            JavaOpcodes.NEW('org/python/types/Slice'),
            JavaOpcodes.DUP(),
        )
        if node.lower:
            self.visit(node.lower)
        else:
            self.context.add_opcodes(
                JavaOpcodes.GETSTATIC('org/python/types/NoneType', 'NONE', 'Lorg/python/Object;')
            )

        if node.upper:
            self.visit(node.upper)
        else:
            self.context.add_opcodes(
                JavaOpcodes.GETSTATIC('org/python/types/NoneType', 'NONE', 'Lorg/python/Object;')
            )

        if node.step:
            self.visit(node.step)
        else:
            self.context.add_opcodes(
                JavaOpcodes.GETSTATIC('org/python/types/NoneType', 'NONE', 'Lorg/python/Object;')
            )

        self.context.add_opcodes(
            JavaOpcodes.INVOKESPECIAL('org/python/types/Slice', '<init>', '(Lorg/python/Object;Lorg/python/Object;Lorg/python/Object;)V')
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
        raise NotImplementedError('No handler for ExceptHandler')
