import unittest
from .utils import TranspileTestCase


class UnaryOpcodeTests(TranspileTestCase):
    def assertUnaryOpcode(self, **kwargs):
        self.assertCode("""
            x = %(x)s
            print(%(operand)sx)
            """ % kwargs)

    @unittest.expectedFailure
    def test_UNARY_POSITIVE(self):
        self.assertUnaryOpcode(x='-42', operand='+', method='__pos__')

    @unittest.expectedFailure
    def test_UNARY_NEGATIVE(self):
        self.assertUnaryOpcode(x='42', operand='-', method='__neg__')

    def test_UNARY_NOT(self):
        self.assertCode("""
            x = True
            print(not x)
            """)

    @unittest.expectedFailure
    def test_UNARY_INVERT(self):
        self.assertUnaryOpcode(x='42', operand='~', method='__invert__')


class BinaryOpcodeTests(TranspileTestCase):
    def assertBinaryOpcode(self, **kwargs):
        self.assertCode("""
            x = 2
            y = 3
            print(%(operation)s)
            """ % kwargs)

    def test_BINARY_POWER(self):
        self.assertBinaryOpcode(operation='x ** y', method="__pow__")

    def test_BINARY_MULTIPLY(self):
        self.assertBinaryOpcode(operation='x * y', method="__mul__")

    @unittest.expectedFailure
    def test_BINARY_MODULO(self):
        self.assertBinaryOpcode(operation='x % y', method="__mod__")

    def test_BINARY_ADD(self):
        self.assertBinaryOpcode(operation='x + y', method="__add__")

    def test_BINARY_SUBTRACT(self):
        self.assertBinaryOpcode(operation='x - y', method="__sub__")

    def test_BINARY_SUBSCR(self):
        self.assertCode("""
            x = [1, 2, 3, 4, 5]
            print(x[2])
            """)

    @unittest.expectedFailure
    def test_BINARY_FLOOR_DIVIDE(self):
        self.assertBinaryOpcode(operation='x // y', method="__floordiv__")

    @unittest.expectedFailure
    def test_BINARY_TRUE_DIVIDE(self):
        self.assertBinaryOpcode(operation='x / y', method="__truediv__")

    @unittest.expectedFailure
    def test_BINARY_LSHIFT(self):
        self.assertBinaryOpcode(operation='x << y', method="__lshift__")

    @unittest.expectedFailure
    def test_BINARY_RSHIFT(self):
        self.assertBinaryOpcode(operation='x >> y', method="__rshift__")

    @unittest.expectedFailure
    def test_BINARY_AND(self):
        self.assertBinaryOpcode(operation='x & y', method="__and__")

    @unittest.expectedFailure
    def test_BINARY_XOR(self):
        self.assertBinaryOpcode(operation='x ^ y', method="__xor__")

    @unittest.expectedFailure
    def test_BINARY_OR(self):
        self.assertBinaryOpcode(operation='x | y', method="__or__")


class InplaceOpcodeTests(TranspileTestCase):
    def assertInplaceOpcode(self, **kwargs):
        self.assertCode("""
            x = 2
            y = 3
            x %(operand)s y
            print(x)
            """ % kwargs)

    @unittest.expectedFailure
    def test_INPLACE_FLOOR_DIVIDE(self):
        self.assertInplaceOpcode(operand='//=', method='__ifloordiv__')

    @unittest.expectedFailure
    def test_INPLACE_TRUE_DIVIDE(self):
        self.assertInplaceOpcode(operand='/=', method='__itruediv__')

    def test_INPLACE_ADD(self):
        self.assertInplaceOpcode(operand='+=', method='__iadd__')

    @unittest.expectedFailure
    def test_INPLACE_SUBTRACT(self):
        self.assertInplaceOpcode(operand='-=', method='__isub__')

    @unittest.expectedFailure
    def test_INPLACE_MULTIPLY(self):
        self.assertInplaceOpcode(operand='*=', method='__imul__')

    @unittest.expectedFailure
    def test_INPLACE_MODULO(self):
        self.assertInplaceOpcode(operand='%=', method='__imod__')

    @unittest.expectedFailure
    def test_INPLACE_POWER(self):
        self.assertInplaceOpcode(operand='**=', method='__ipow__')

    @unittest.expectedFailure
    def test_INPLACE_LSHIFT(self):
        self.assertInplaceOpcode(operand='<<=', method='__ilshift__')

    @unittest.expectedFailure
    def test_INPLACE_RSHIFT(self):
        self.assertInplaceOpcode(operand='>>=', method='__irshift__')

    @unittest.expectedFailure
    def test_INPLACE_AND(self):
        self.assertInplaceOpcode(operand='&=', method='__iand__')

    @unittest.expectedFailure
    def test_INPLACE_XOR(self):
        self.assertInplaceOpcode(operand='^=', method='__ixor__')

    @unittest.expectedFailure
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
