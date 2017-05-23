from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase

from unittest import expectedFailure


class BytesTests(TranspileTestCase):
    def test_setattr(self):
        self.assertCodeExecution("""
            x = b'hello, world'
            try:
                x.attr = 42
            except AttributeError as err:
                print(err)
            """)

    def test_getattr(self):
        self.assertCodeExecution("""
            x = b'hello, world'
            try:
                print(x.attr)
            except AttributeError as err:
                print(err)
            """)

    def test_capitalize(self):
        self.assertCodeExecution("""
            print(b'hello, world'.capitalize())
            print(b'helloWORLD'.capitalize())
            print(b'HELLO WORLD'.capitalize())
            print(b'2015638687'.capitalize())
        """)

    @expectedFailure
    def test_capitalize_with_nonascii(self):
        # Move this to test_capitalize upon resolution of #530
        self.assertCodeExecution("""
            print(b'\xc8'.capitalize())
        """)

    def test_iter(self):
        self.assertCodeExecution("""
            print([b for b in b''])
            print([b for b in b'hello world'])
        """)

    def test_find(self):
        self.assertCodeExecution("""
            print(b''.find(b'a'))
            print(b'abcd'.find(b''))
            print(b'abcd'.find(b'...'))
            print(b'abcd'.find(b'ab'))
            print(b'abcd'.find(b'bc'))
            print(b'abcd'.find(b'cd'))
            print(b'abcd'.find(b'cd', 2))
            print(b'abcd'.find(b'ab', 3))
            print(b'abcd'.find(b'cd', 2, 3))
            print(b'abcd'.find(b'ab', 3, 4))
        """)


class UnaryBytesOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'bytes'

    not_implemented = [
    ]


class BinaryBytesOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'bytes'

    not_implemented = [
        'test_add_class',
        'test_add_frozenset',

        'test_and_class',
        'test_and_frozenset',

        'test_direct_eq_bool',
        'test_direct_eq_bytearray',
        'test_direct_eq_bytes',
        'test_direct_eq_class',
        'test_direct_eq_complex',
        'test_direct_eq_dict',
        'test_direct_eq_float',
        'test_direct_eq_frozenset',
        'test_direct_eq_int',
        'test_direct_eq_list',
        'test_direct_eq_none',
        'test_direct_eq_set',
        'test_direct_eq_str',
        'test_direct_eq_tuple',

        'test_direct_ge_bool',
        'test_direct_ge_bytearray',
        'test_direct_ge_bytes',
        'test_direct_ge_class',
        'test_direct_ge_complex',
        'test_direct_ge_dict',
        'test_direct_ge_float',
        'test_direct_ge_frozenset',
        'test_direct_ge_int',
        'test_direct_ge_list',
        'test_direct_ge_none',
        'test_direct_ge_set',
        'test_direct_ge_str',
        'test_direct_ge_tuple',

        'test_direct_gt_bool',
        'test_direct_gt_bytearray',
        'test_direct_gt_bytes',
        'test_direct_gt_class',
        'test_direct_gt_complex',
        'test_direct_gt_dict',
        'test_direct_gt_float',
        'test_direct_gt_frozenset',
        'test_direct_gt_int',
        'test_direct_gt_list',
        'test_direct_gt_none',
        'test_direct_gt_set',
        'test_direct_gt_str',
        'test_direct_gt_tuple',

        'test_direct_le_bool',
        'test_direct_le_bytearray',
        'test_direct_le_bytes',
        'test_direct_le_class',
        'test_direct_le_complex',
        'test_direct_le_dict',
        'test_direct_le_float',
        'test_direct_le_frozenset',
        'test_direct_le_int',
        'test_direct_le_list',
        'test_direct_le_none',
        'test_direct_le_set',
        'test_direct_le_str',
        'test_direct_le_tuple',

        'test_direct_lt_bool',
        'test_direct_lt_bytearray',
        'test_direct_lt_bytes',
        'test_direct_lt_class',
        'test_direct_lt_complex',
        'test_direct_lt_dict',
        'test_direct_lt_float',
        'test_direct_lt_frozenset',
        'test_direct_lt_int',
        'test_direct_lt_list',
        'test_direct_lt_none',
        'test_direct_lt_set',
        'test_direct_lt_str',
        'test_direct_lt_tuple',

        'test_direct_ne_bool',
        'test_direct_ne_bytearray',
        'test_direct_ne_bytes',
        'test_direct_ne_class',
        'test_direct_ne_complex',
        'test_direct_ne_dict',
        'test_direct_ne_float',
        'test_direct_ne_frozenset',
        'test_direct_ne_int',
        'test_direct_ne_list',
        'test_direct_ne_none',
        'test_direct_ne_set',
        'test_direct_ne_str',
        'test_direct_ne_tuple',

        'test_direct_eq_frozenset',
        'test_direct_ge_frozenset',
        'test_direct_gt_frozenset',
        'test_direct_le_frozenset',
        'test_direct_lt_frozenset',
        'test_direct_ne_frozenset',

        'test_eq_bytearray',
        'test_eq_bytes',
        'test_eq_frozenset',

        'test_ne_frozenset',

        'test_ge_frozenset',

        'test_gt_frozenset',

        'test_le_frozenset',

        'test_lt_frozenset',

        'test_lshift_class',
        'test_lshift_frozenset',

        'test_modulo_None',
        'test_modulo_NotImplemented',
        'test_modulo_bool',
        'test_modulo_bytearray',
        'test_modulo_bytes',
        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_dict',
        'test_modulo_float',
        'test_modulo_frozenset',
        'test_modulo_int',
        'test_modulo_list',
        'test_modulo_range',
        'test_modulo_set',
        'test_modulo_slice',
        'test_modulo_str',
        'test_modulo_tuple',

        'test_multiply_class',
        'test_multiply_frozenset',

        'test_or_class',
        'test_or_frozenset',

        'test_power_class',
        'test_power_frozenset',

        'test_rshift_class',
        'test_rshift_frozenset',

        'test_subscr_class',
        'test_subscr_frozenset',

        'test_subtract_class',
        'test_subtract_frozenset',

        'test_true_divide_class',
        'test_true_divide_frozenset',

        'test_xor_class',
        'test_xor_frozenset',
    ]


class InplaceBytesOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'bytes'

    not_implemented = [
        'test_add_class',
        'test_add_frozenset',

        'test_and_class',
        'test_and_frozenset',

        'test_floor_divide_class',
        'test_floor_divide_complex',
        'test_floor_divide_frozenset',

        'test_lshift_class',
        'test_lshift_frozenset',

        'test_modulo_None',
        'test_modulo_NotImplemented',
        'test_modulo_bool',
        'test_modulo_bytearray',
        'test_modulo_bytes',
        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_dict',
        'test_modulo_float',
        'test_modulo_frozenset',
        'test_modulo_int',
        'test_modulo_list',
        'test_modulo_range',
        'test_modulo_set',
        'test_modulo_slice',
        'test_modulo_str',
        'test_modulo_tuple',

        'test_multiply_class',
        'test_multiply_frozenset',

        'test_or_class',
        'test_or_frozenset',

        'test_power_class',
        'test_power_frozenset',

        'test_rshift_class',
        'test_rshift_frozenset',

        'test_subtract_class',
        'test_subtract_frozenset',

        'test_true_divide_class',
        'test_true_divide_frozenset',

        'test_xor_class',
        'test_xor_frozenset',
    ]
