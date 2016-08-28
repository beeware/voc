from unittest import expectedFailure

from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class BytearrayTests(TranspileTestCase):
    def test_setattr(self):
        self.assertCodeExecution("""
            x = bytearray([1,2,3])
            x.attr = 42
            print('Done.')
            """)

    def test_getattr(self):
        self.assertCodeExecution("""
            x = bytearray([1,2,3])
            print(x.attr)
            print('Done.')
            """)


class UnaryBytearrayOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'bytearray'

    not_implemented = [
    ]


class BinaryBytearrayOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'bytearray'

    not_implemented = [
        'test_add_class',
        'test_add_complex',
        'test_add_frozenset',

        'test_and_class',
        'test_and_complex',
        'test_and_frozenset',

        'test_eq_class',
        'test_eq_complex',
        'test_eq_frozenset',

        'test_floor_divide_class',
        'test_floor_divide_complex',
        'test_floor_divide_frozenset',

        'test_ge_class',
        'test_ge_complex',
        'test_ge_frozenset',

        'test_gt_class',
        'test_gt_complex',
        'test_gt_frozenset',

        'test_le_class',
        'test_le_complex',
        'test_le_frozenset',

        'test_lshift_class',
        'test_lshift_complex',
        'test_lshift_frozenset',

        'test_lt_class',
        'test_lt_complex',
        'test_lt_frozenset',

        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_frozenset',

        'test_multiply_class',
        'test_multiply_complex',
        'test_multiply_frozenset',

        'test_ne_class',
        'test_ne_complex',
        'test_ne_frozenset',

        'test_or_class',
        'test_or_complex',
        'test_or_frozenset',

        'test_power_class',
        'test_power_complex',
        'test_power_frozenset',

        'test_rshift_class',
        'test_rshift_complex',
        'test_rshift_frozenset',

        'test_subscr_class',
        'test_subscr_complex',
        'test_subscr_frozenset',

        'test_subtract_class',
        'test_subtract_complex',
        'test_subtract_frozenset',

        'test_true_divide_class',
        'test_true_divide_complex',
        'test_true_divide_frozenset',

        'test_xor_class',
        'test_xor_complex',
        'test_xor_frozenset',
    ]


class InplaceBytearrayOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'bytearray'

    not_implemented = [
        'test_add_class',
        'test_add_complex',
        'test_add_frozenset',

        'test_and_class',
        'test_and_complex',
        'test_and_frozenset',

        'test_floor_divide_class',
        'test_floor_divide_complex',
        'test_floor_divide_frozenset',

        'test_lshift_class',
        'test_lshift_complex',
        'test_lshift_frozenset',

        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_frozenset',

        'test_multiply_class',
        'test_multiply_complex',
        'test_multiply_frozenset',

        'test_or_class',
        'test_or_complex',
        'test_or_frozenset',

        'test_power_class',
        'test_power_complex',
        'test_power_frozenset',

        'test_rshift_class',
        'test_rshift_complex',
        'test_rshift_frozenset',

        'test_subtract_class',
        'test_subtract_complex',
        'test_subtract_frozenset',

        'test_true_divide_class',
        'test_true_divide_complex',
        'test_true_divide_frozenset',

        'test_xor_class',
        'test_xor_complex',
        'test_xor_frozenset',
    ]
