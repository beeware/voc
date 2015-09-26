from .utils import TranspileTestCase


class UnaryOpcodeTests(TranspileTestCase):
    def assertUnaryOpcode(self, **kwargs):
        self.assertBlock(
            python="""
                x = %(x)s
                y = %(operand)sx
                """ % kwargs,
            java="""
                 Code (48 bytes)
                     Max stack: 3
                     Max locals: 2
                     Bytecode: (20 bytes)
                           0: <NEW org/python/types/Int>
                           3: <DUP>
                           4: <SIPUSH %(x)s>
                           7: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          10: <ASTORE_0>
                          11: <ALOAD_0>
                          12: <INVOKEINTERFACE org/python/Object.%(method)s ()Lorg/python/Object;>
                          17: <ASTORE_1>
                          18: <ACONST_NULL>
                          19: <ARETURN>
                     Exceptions: (0)
                     Attributes: (1)
                         LineNumberTable (10 bytes)
                             Line numbers (2 total):
                                 0: 2
                                 11: 3
                """ % kwargs)

    def test_UNARY_POSITIVE(self):
        self.assertUnaryOpcode(x='-42', operand='+', method='__pos__')

    def test_UNARY_NEGATIVE(self):
        self.assertUnaryOpcode(x='42', operand='-', method='__neg__')

    def test_UNARY_NOT(self):
        self.assertBlock(
            python="""
                x = True
                y = not x
                """,
            java="""
                 Code (46 bytes)
                     Max stack: 3
                     Max locals: 2
                     Bytecode: (18 bytes)
                           0: <NEW org/python/types/Bool>
                           3: <DUP>
                           4: <ICONST_1>
                           5: <INVOKESPECIAL org/python/types/Bool.<init> (Z)V>
                           8: <ASTORE_0>
                           9: <ALOAD_0>
                          10: <INVOKEINTERFACE org/python/Object.__not__ ()Lorg/python/Object;>
                          15: <ASTORE_1>
                          16: <ACONST_NULL>
                          17: <ARETURN>
                     Exceptions: (0)
                     Attributes: (1)
                         LineNumberTable (10 bytes)
                             Line numbers (2 total):
                                 0: 2
                                 9: 3
                """)

    def test_UNARY_INVERT(self):
        self.assertUnaryOpcode(x='42', operand='~', method='__invert__')


class BinaryOpcodeTests(TranspileTestCase):
    def assertBinaryOpcode(self, **kwargs):
        self.assertBlock(
            python="""
                x = 42
                y = 37
                z = %(operation)s
                """ % kwargs,
            java="""
                 Code (64 bytes)
                     Max stack: 3
                     Max locals: 3
                     Bytecode: (32 bytes)
                           0: <NEW org/python/types/Int>
                           3: <DUP>
                           4: <SIPUSH 42>
                           7: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          10: <ASTORE_0>
                          11: <NEW org/python/types/Int>
                          14: <DUP>
                          15: <SIPUSH 37>
                          18: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          21: <ASTORE_1>
                          22: <ALOAD_0>
                          23: <ALOAD_1>
                          24: <INVOKEINTERFACE org/python/Object.%(method)s (Lorg/python/Object;)Lorg/python/Object;>
                          29: <ASTORE_2>
                          30: <ACONST_NULL>
                          31: <ARETURN>
                     Exceptions: (0)
                     Attributes: (1)
                         LineNumberTable (14 bytes)
                             Line numbers (3 total):
                                 0: 2
                                 11: 3
                                 22: 4
                """ % kwargs)

    def test_BINARY_POWER(self):
        self.assertBinaryOpcode(operation='x ** y', method="__pow__")

    def test_BINARY_MULTIPLY(self):
        self.assertBinaryOpcode(operation='x * y', method="__mul__")

    def test_BINARY_MODULO(self):
        self.assertBinaryOpcode(operation='x % y', method="__mod__")

    def test_BINARY_ADD(self):
        self.assertBinaryOpcode(operation='x + y', method="__add__")

    def test_BINARY_SUBTRACT(self):
        self.assertBinaryOpcode(operation='x - y', method="__sub__")

    def test_BINARY_SUBSCR(self):
        self.assertBinaryOpcode(operation='x[y]', method="__getitem__")

    def test_BINARY_FLOOR_DIVIDE(self):
        self.assertBinaryOpcode(operation='x // y', method="__floordiv__")

    def test_BINARY_TRUE_DIVIDE(self):
        self.assertBinaryOpcode(operation='x / y', method="__truediv__")

    def test_BINARY_LSHIFT(self):
        self.assertBinaryOpcode(operation='x << y', method="__lshift__")

    def test_BINARY_RSHIFT(self):
        self.assertBinaryOpcode(operation='x >> y', method="__rshift__")

    def test_BINARY_AND(self):
        self.assertBinaryOpcode(operation='x & y', method="__and__")

    def test_BINARY_XOR(self):
        self.assertBinaryOpcode(operation='x ^ y', method="__xor__")

    def test_BINARY_OR(self):
        self.assertBinaryOpcode(operation='x | y', method="__or__")


class InplaceOpcodeTests(TranspileTestCase):
    def assertInplaceOpcode(self, **kwargs):
        self.assertBlock(
            python="""
                x = 42
                x %(operand)s x
                """ % kwargs,
            java="""
                 Code (50 bytes)
                     Max stack: 3
                     Max locals: 1
                     Bytecode: (22 bytes)
                           0: <NEW org/python/types/Int>
                           3: <DUP>
                           4: <SIPUSH 42>
                           7: <INVOKESPECIAL org/python/types/Int.<init> (I)V>
                          10: <ASTORE_0>
                          11: <ALOAD_0>
                          12: <DUP>
                          13: <ALOAD_0>
                          14: <INVOKEINTERFACE org/python/Object.%(method)s (Lorg/python/Object;)V>
                          19: <ASTORE_0>
                          20: <ACONST_NULL>
                          21: <ARETURN>
                     Exceptions: (0)
                     Attributes: (1)
                         LineNumberTable (10 bytes)
                             Line numbers (2 total):
                                 0: 2
                                 11: 3
                """ % kwargs)

    def test_INPLACE_FLOOR_DIVIDE(self):
        self.assertInplaceOpcode(operand='//=', method='__ifloordiv__')

    def test_INPLACE_TRUE_DIVIDE(self):
        self.assertInplaceOpcode(operand='/=', method='__itruediv__')

    def test_INPLACE_ADD(self):
        self.assertInplaceOpcode(operand='+=', method='__iadd__')

    def test_INPLACE_SUBTRACT(self):
        self.assertInplaceOpcode(operand='-=', method='__isub__')

    def test_INPLACE_MULTIPLY(self):
        self.assertInplaceOpcode(operand='*=', method='__imul__')

    def test_INPLACE_MODULO(self):
        self.assertInplaceOpcode(operand='%=', method='__imod__')

    def test_INPLACE_POWER(self):
        self.assertInplaceOpcode(operand='**=', method='__ipow__')

    def test_INPLACE_LSHIFT(self):
        self.assertInplaceOpcode(operand='<<=', method='__ilshift__')

    def test_INPLACE_RSHIFT(self):
        self.assertInplaceOpcode(operand='>>=', method='__irshift__')

    def test_INPLACE_AND(self):
        self.assertInplaceOpcode(operand='&=', method='__iand__')

    def test_INPLACE_XOR(self):
        self.assertInplaceOpcode(operand='^=', method='__ixor__')

    def test_INPLACE_OR(self):
        self.assertInplaceOpcode(operand='|=', method='__ior__')


# class StackOpcodeTests(TranspileTestCase):
    # def test_POP_TOP(self):
    # def test_ROT_TWO(self):
    # def test_ROT_THREE(self):
    # def test_DUP_TOP(self):
    # def test_DUP_TOP_TWO(self):
    # def test_NOP(self):




# STORE_MAP

# STORE_SUBSCR
# DELETE_SUBSCR


# GET_ITER
# PRINT_EXPR
# LOAD_BUILD_CLASS
# YIELD_FROM

# BREAK_LOOP
# WITH_CLEANUP

# RETURN_VALUE
# IMPORT_STAR

# YIELD_VALUE
# POP_BLOCK
# END_FINALLY
# POP_EXCEPT

# HAVE_ARGUMENT

# STORE_NAME
# DELETE_NAME
# UNPACK_SEQUENCE
# FOR_ITER
# UNPACK_EX

# STORE_ATTR
# DELETE_ATTR
# STORE_GLOBAL
# DELETE_GLOBAL

# LOAD_CONST
# LOAD_NAME
# BUILD_TUPLE
# BUILD_LIST
# BUILD_SET
# BUILD_MAP
# LOAD_ATTR
# COMPARE_OP
# IMPORT_NAME
# IMPORT_FROM

# JUMP_FORWARD
# JUMP_IF_FALSE_OR_POP
# JUMP_IF_TRUE_OR_POP
# JUMP_ABSOLUTE
# POP_JUMP_IF_FALSE
# POP_JUMP_IF_TRUE

# LOAD_GLOBAL

# CONTINUE_LOOP
# SETUP_LOOP
# SETUP_EXCEPT
# SETUP_FINALLY

# LOAD_FAST
# STORE_FAST
# DELETE_FAST

# RAISE_VARARGS
# CALL_FUNCTION
# MAKE_FUNCTION
# BUILD_SLICE

# MAKE_CLOSURE
# LOAD_CLOSURE
# LOAD_DEREF
# STORE_DEREF
# DELETE_DEREF

# CALL_FUNCTION_KW
# CALL_FUNCTION_VAR_KW

# SETUP_WITH

# LIST_APPEND
# SET_ADD
# MAP_ADD

# LOAD_CLASSDEREF
