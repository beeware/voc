from unittest import expectedFailure

from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class BytesTests(TranspileTestCase):
    def test_setattr(self):
        self.assertCodeExecution("""
            x = b'hello, world'
            x.attr = 42
            print('Done.')
            """)

    def test_getattr(self):
        self.assertCodeExecution("""
            x = b'hello, world'
            print(x.attr)
            print('Done.')
            """)


class UnaryBytesOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'bytes'

    not_implemented = [
    ]


class BinaryBytesOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'bytes'

    not_implemented = [
        'test_add_class',
        'test_add_complex',
        'test_add_dict',
        'test_add_frozenset',

        'test_and_class',
        'test_and_complex',
        'test_and_dict',
        'test_and_frozenset',

        'test_eq_class',
        'test_eq_complex',
        'test_eq_dict',
        'test_eq_frozenset',

        'test_ne_class',
        'test_ne_complex',
        'test_ne_dict',
        'test_ne_frozenset',

        'test_floor_divide_class',
        'test_floor_divide_complex',
        'test_floor_divide_dict',
        'test_floor_divide_frozenset',

        'test_ge_bytearray',
        'test_ge_bytes',
        'test_ge_class',
        'test_ge_complex',
        'test_ge_dict',
        'test_ge_frozenset',

        'test_gt_bytearray',
        'test_gt_bytes',
        'test_gt_class',
        'test_gt_complex',
        'test_gt_dict',
        'test_gt_frozenset',

        'test_le_bytearray',
        'test_le_bytes',
        'test_le_class',
        'test_le_complex',
        'test_le_dict',
        'test_le_frozenset',

        'test_lt_bytearray',
        'test_lt_bytes',
        'test_lt_class',
        'test_lt_complex',
        'test_lt_dict',
        'test_lt_frozenset',

        'test_lshift_class',
        'test_lshift_complex',
        'test_lshift_dict',
        'test_lshift_frozenset',

        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_dict',
        'test_modulo_frozenset',
        'test_modulo_None',
        'test_modulo_NotImplemented',
        'test_modulo_bool',
        'test_modulo_bytearray',
        'test_modulo_bytes',
        'test_modulo_float',
        'test_modulo_int',
        'test_modulo_list',
        'test_modulo_range',
        'test_modulo_set',
        'test_modulo_slice',
        'test_modulo_str',
        'test_modulo_tuple',

        'test_multiply_class',
        'test_multiply_complex',
        'test_multiply_dict',
        'test_multiply_frozenset',

        'test_or_class',
        'test_or_complex',
        'test_or_dict',
        'test_or_frozenset',

        'test_power_class',
        'test_power_complex',
        'test_power_dict',
        'test_power_frozenset',

        'test_rshift_class',
        'test_rshift_complex',
        'test_rshift_dict',
        'test_rshift_frozenset',

        'test_subscr_class',
        'test_subscr_complex',
        'test_subscr_dict',
        'test_subscr_frozenset',

        'test_subtract_class',
        'test_subtract_complex',
        'test_subtract_dict',
        'test_subtract_frozenset',

        'test_true_divide_class',
        'test_true_divide_complex',
        'test_true_divide_dict',
        'test_true_divide_frozenset',

        'test_xor_class',
        'test_xor_complex',
        'test_xor_dict',
        'test_xor_frozenset',
    ]


class InplaceBytesOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'bytes'

    not_implemented = [
        'test_add_bool',
        'test_add_bytearray',
        'test_add_bytes',
        'test_add_class',
        'test_add_complex',
        'test_add_dict',
        'test_add_float',
        'test_add_frozenset',
        'test_add_int',
        'test_add_list',
        'test_add_None',
        'test_add_NotImplemented',
        'test_add_range',
        'test_add_set',
        'test_add_slice',
        'test_add_str',
        'test_add_tuple',

        'test_and_class',
        'test_and_complex',
        'test_and_dict',
        'test_and_frozenset',

        'test_floor_divide_class',
        'test_floor_divide_complex',
        'test_floor_divide_dict',
        'test_floor_divide_frozenset',

        'test_lshift_class',
        'test_lshift_complex',
        'test_lshift_dict',
        'test_lshift_frozenset',

        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_frozenset',
        'test_modulo_None',
        'test_modulo_NotImplemented',
        'test_modulo_bool',
        'test_modulo_bytearray',
        'test_modulo_bytes',
        'test_modulo_dict',
        'test_modulo_float',
        'test_modulo_int',
        'test_modulo_list',
        'test_modulo_range',
        'test_modulo_set',
        'test_modulo_slice',
        'test_modulo_str',
        'test_modulo_tuple',

        'test_multiply_bool',
        'test_multiply_bytearray',
        'test_multiply_bytes',
        'test_multiply_class',
        'test_multiply_complex',
        'test_multiply_dict',
        'test_multiply_float',
        'test_multiply_frozenset',
        'test_multiply_int',
        'test_multiply_list',
        'test_multiply_None',
        'test_multiply_NotImplemented',
        'test_multiply_range',
        'test_multiply_set',
        'test_multiply_slice',
        'test_multiply_str',
        'test_multiply_tuple',

        'test_or_class',
        'test_or_complex',
        'test_or_dict',
        'test_or_frozenset',

        'test_power_class',
        'test_power_complex',
        'test_power_dict',
        'test_power_frozenset',

        'test_rshift_class',
        'test_rshift_complex',
        'test_rshift_dict',
        'test_rshift_frozenset',

        'test_subtract_class',
        'test_subtract_complex',
        'test_subtract_dict',
        'test_subtract_frozenset',

        'test_true_divide_class',
        'test_true_divide_complex',
        'test_true_divide_dict',
        'test_true_divide_frozenset',

        'test_xor_class',
        'test_xor_complex',
        'test_xor_dict',
        'test_xor_frozenset',
    ]
