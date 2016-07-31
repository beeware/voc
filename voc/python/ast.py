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
        if node.lineno != self._current_line:
            self._current_line = self.context.next_opcode_starts_line = node.lineno
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

        # @node_visitor
    # def visit_Interactive(self, node):
    #     # stmt* body):
    #     print("Interactive", dir(node)))
    #     self.generic_visit(node)

    # @node_visitor
    # def visit_Expr(self, node):
    #     print("Expression", node)
    #     self.generic_visit(node)

    # @node_visitor
    # def visit_Suite(self, node):
    #     # stmt* body):
    #     print("Suite", dir(node)))
    #     self.generic_visit(node)

    # # Statements
    @node_visitor
    def visit_FunctionDef(self, node):
        # identifier name, arguments args, stmt* body, expr* decorator_list, expr? returns):
        method = self.context.add_method(node)

        self._context.append(method)
        for child in node.body:
            self.visit(child)
        self._context.pop()

        # @node_visitor
    # def visit_ClassDef(self, node):
    #     # identifier name, expr* bases, keyword* keywords, expr? starargs, expr? kwargs, stmt* body, expr* decorator_list):
    #     print("ClassDef", dir(node)))
    #     self.generic_visit(node)

    # @node_visitor
    # def visit_Return(self, node):
    #     # expr? value):
    #     print("Return", dir(node)))
    #     self.generic_visit(node)

    # @node_visitor
    # def visit_Delete(self, node):
    #     # expr* targets):
    #     print("Delete", dir(node)))
    #     self.generic_visit(node)

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
                self.context.store_name(target.id, use_locals=False)
            self.context.add_opcodes(
                JavaOpcodes.POP()
            )
        else:
            self.context.store_name(node.targets[0].id, use_locals=False)


            # @node_visitor
    # def visit_AugAssign(self, node):
    #     # expr target, operator op, expr value):
    #     print("AugAssign", dir(node)))
    #     self.generic_visit(node)

    # @node_visitor
    # def visit_For(self, node):
    #     # expr target, expr iter, stmt* body, stmt* orelse):
    #     print("For", dir(node)))
    #     self.generic_visit(node)

    # @node_visitor
    # def visit_While(self, node):
    #     # expr test, stmt* body, stmt* orelse):
    #     print("While", dir(node)))
    #     self.generic_visit(node)

    @node_visitor
    def visit_If(self, node):
        # expr test, stmt* body, stmt* orelse):
        self.visit(node.test)

        self.context.add_opcodes(
            JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__bool__', '()Lorg/python/Object;'),
            JavaOpcodes.CHECKCAST('org/python/types/Bool'),
            JavaOpcodes.GETFIELD('org/python/types/Bool', 'value', 'Z'),
            jump(JavaOpcodes.IFEQ(0), self.context, node, OpcodePosition.ELSE),
        )

        for child in node.body:
            self.visit(child)

        self.context.add_opcodes(
            jump(JavaOpcodes.GOTO(0), self.context, node, OpcodePosition.END),
        )
        self.context.next_resolve_list.append((node, OpcodePosition.ELSE))

        for child in node.orelse:
            self.visit(child)


    # @node_visitor
    # def visit_With(self, node):
    #     # withitem* items, stmt* body):
    #     print("With", dir(node)))
    #     self.generic_visit(node)

    # @node_visitor
    # def visit_Raise(self, node):
    #     # expr? exc, expr? cause):
    #     print("Raise", dir(node)))
    #     self.generic_visit(node)

    # @node_visitor
    # def visit_Try(self, node):
    #     # stmt* body, excepthandler* handlers, stmt* orelse, stmt* finalbody):
    #     print("Try", dir(node)))
    #     self.generic_visit(node)

    # @node_visitor
    # def visit_Assert(self, node):
    #     # expr test, expr? msg):
    #     print("Assert", dir(node)))
    #     self.generic_visit(node)

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

    # @node_visitor
    # def visit_Global(self, node):
    #     # identifier* names):
    #     print("Global", dir(node)))
    #     self.generic_visit(node)

    # @node_visitor
    # def visit_Nonlocal(self, node):
    #     # identifier* names):
    #     print("Nonlocal", dir(node)))
    #     self.generic_visit(node)

    # @node_visitor
    # def visit_Expr(self, node):
    #     # expr value):
    #     print("Expr", dir(node)))
    #     self.generic_visit(node)


    # @node_visitor
    # def visit_Pass(self, node):
    # #
    #     print("Pass", dir(node))
    #     self.generic_visit(node)

    # @node_visitor
    # def visit_Break(self, node):
    # #
    #     print("Break", dir(node))
    #     self.generic_visit(node)

    # @node_visitor
    # def visit_Continue(self, node):
    # #
    #     print("Continue", dir(node))
    #     self.generic_visit(node)

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

    # @node_visitor
    # def visit_BinOp(self, node):
    #     # expr left, operator op, expr right):
    #     print("BinOp", dir(node)))
    #     self.generic_visit(node)

    # @node_visitor
    # def visit_UnaryOp(self, node):
    #     # unaryop op, expr operand):
    #     print("UnaryOp", dir(node)))
    #     self.generic_visit(node)

    # @node_visitor
    # def visit_Lambda(self, node):
    #     # arguments args, expr body):
    #     print("Lambda", dir(node)))
    #     self.generic_visit(node)

    @node_visitor
    def visit_IfExp(self, node):
        self.visit(node.test)

        self.context.add_opcodes(
            JavaOpcodes.INVOKEINTERFACE('org/python/Object', '__bool__', '()Lorg/python/Object;'),
            JavaOpcodes.CHECKCAST('org/python/types/Bool'),
            JavaOpcodes.GETFIELD('org/python/types/Bool', 'value', 'Z'),
            jump(JavaOpcodes.IFEQ(0), self.context, node, OpcodePosition.ELSE),
        )

        self.visit(node.body)

        self.context.add_opcodes(
            jump(JavaOpcodes.GOTO(0), self.context, node, OpcodePosition.END),
        )
        self.context.next_resolve_list.append((node, OpcodePosition.ELSE))

        self.visit(node.orelse)

    # @node_visitor
    # def visit_Dict(self, node):
    #     # expr* keys, expr* values):
    #     print("Dict", dir(node)))
    #     self.generic_visit(node)

    # @node_visitor
    # def visit_Set(self, node):
    #     expr* elts):
    #     print("Set", dir(node)))
    #     self.generic_visit(node)

    # @node_visitor
    # def visit_ListComp(self, node):
    #     expr elt, comprehension* generators):
    #     print("ListComp", dir(node)))
    #     self.generic_visit(node)

    # @node_visitor
    # def visit_SetComp(self, node):
    #     expr elt, comprehension* generators):
    #     print("SetComp", dir(node)))
    #     self.generic_visit(node)

    # @node_visitor
    # def visit_DictComp(self, node):
    #     expr key, expr value, comprehension* generators):
    #     print("DictComp", dir(node)))
    #     self.generic_visit(node)

    # @node_visitor
    # def visit_GeneratorExp(self, node):
    #     expr elt, comprehension* generators):
    #     print("GeneratorExp", dir(node)))
    #     self.generic_visit(node)


    # @node_visitor
    # def visit_Yield(self, node):
    #     expr? value):
    #     print("Yield", dir(node)))
    #     self.generic_visit(node)

    # @node_visitor
    # def visit_YieldFrom(self, node):
    #     expr value):
    #     print("YieldFrom", dir(node)))
    #     self.generic_visit(node)

    @node_visitor
    def visit_Compare(self, node):
        self.visit(node.left)
        const_comparison = type(node.left) == ast.Num

        if len(node.comparators) == 1:
            self.visit(node.comparators[0])
            const_comparison |= type(node.comparators[0]) == ast.Num
        else:
            raise Exception("Don't know how to resolve multiple comparators")

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
                self.context.add_opcodes(
                    JavaOpcodes.INVOKEINTERFACE(
                        'org/python/Object',
                        {
                            ast.Eq: '__eq__',
                            ast.Gt: '__gt__',
                            ast.GtE: '__ge__',
                            ast.Lt: '__lt__',
                            ast.LtE: '__le__',
                            ast.Is: '__eq__',
                            ast.IsNot: '__ne__',
                            ast.NotEq: '__ne__',
                        }[type(node.ops[0])],
                        '(Lorg/python/Object;)Lorg/python/Object;'
                    )
                )
        else:
            raise Exception("Don't know how to resolve multiple operators")

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
            raise Exception('Unknown number type')

    @node_visitor
    def visit_Str(self, node):
        "Load a string constant"
        self.context.add_str(node.s)

        # @node_visitor
    # def visit_Bytes(self, node):
    #     bytes s):
    #     print("Bytes", dir(node)))
    #     self.generic_visit(node)

    @node_visitor
    def visit_NameConstant(self, node):
        if node.value is None:
            self.context.add_opcodes(
                JavaOpcodes.GETSTATIC('org/python/types/NoneType', 'NONE', 'Lorg/python/Object;')
            )
        else:
            raise Exception("Unknown named constant %s" % node.value)

    # @node_visitor
    # def visit_Ellipsis(self, node):
    # #
    #      print("Ellipsis", dir(node))
    #      self.generic_visit(node)


    # @node_visitor
    # def visit_Attribute(self, node):
    #     expr value, identifier attr, expr_context ctx):
    #     print("Attribute", dir(node)))
    #     self.generic_visit(node)

    # @node_visitor
    # def visit_Subscript(self, node):
    #     expr value, slice slice, expr_context ctx):
    #     print("Subscript", dir(node)))
    #     self.generic_visit(node)

    # @node_visitor
    # def visit_Starred(self, node):
    #     expr value, expr_context ctx):
    #     print("Starred", dir(node)))
    #     self.generic_visit(node)

    @node_visitor
    def visit_Name(self, node):
        self.context.load_name(node.id, use_locals=True)

        # @node_visitor
    # def visit_List(self, node):
    #     expr* elts, expr_context ctx):
    #     print("List", dir(node)))
    #     self.generic_visit(node)

    # @node_visitor
    # def visit_Tuple(self, node):
    #     expr* elts, expr_context ctx):
    #     print("Tuple", dir(node)))
    #     self.generic_visit(node)


    # @node_visitor
    # def visit_Slice(self, node):
    #     expr? lower, expr? upper, expr? step):
    #     print("Slice", dir(node)))
    #     self.generic_visit(node)

    # @node_visitor
    # def visit_ExtSlice(self, node):
    #     slice* dims):
    #     print("ExtSlice", dir(node)))
    #     self.generic_visit(node)

    # @node_visitor
    # def visit_Index(self, node):
    #     expr value):
    #     print("Index", dir(node)))
    #     self.generic_visit(node)


    # @node_visitor
    # def visit_ExceptHandler(self, node):
    #     expr? type, identifier? name, stmt* body):
    #     print("ExceptHandler", dir(node)))
    #     self.generic_visit(node)
