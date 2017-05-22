from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class NoneTypeTests(TranspileTestCase):
    def test_setattr(self):
        self.assertCodeExecution("""
            x = None
            try:
                x.thing = 42
            except AttributeError as err:
                print(err)
            """)

    def test_getattr(self):
        self.assertCodeExecution("""
            x = None
            try:
                y = x.thing
            except AttributeError as err:
                print(err)
            """)


class UnaryNoneTypeOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'None'


class BinaryNoneTypeOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'None'

    not_implemented = [
        'test_add_class',


        'test_direct_ne_bool',
        'test_direct_ne_class',
        'test_direct_ne_complex',
        'test_direct_ne_dict',
        'test_direct_ne_float',
        'test_direct_ne_frozenset',
        'test_direct_ne_int',
        'test_direct_ne_NotImplemented',
        'test_direct_ne_range',
        'test_direct_ne_set',
        'test_direct_ne_slice',
        'test_direct_ne_str',

        'test_direct_le_bytes',
        'test_direct_lt_bytes',

        'test_direct_ge_frozenset',
        'test_direct_gt_frozenset',
        'test_direct_le_frozenset',
        'test_direct_lt_frozenset',

        'test_eq_class',

        'test_ge_class',

        'test_gt_class',

        'test_le_class',
        'test_le_frozenset',

        'test_lshift_class',
        'test_lshift_frozenset',

        'test_lt_class',
        'test_lt_frozenset',

        'test_modulo_class',
        'test_modulo_complex',

        'test_multiply_bytes',
        'test_multiply_bytearray',
        'test_multiply_class',

        'test_ne_class',
        'test_ne_frozenset',

        'test_or_class',
        'test_or_frozenset',

        'test_power_class',

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


class InplaceNoneTypeOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'None'

    not_implemented = [
        'test_add_frozenset',

        'test_and_class',

        'test_floor_divide_class',
        'test_floor_divide_complex',

        'test_lshift_class',
        'test_lshift_frozenset',

        'test_modulo_complex',

        'test_multiply_bytes',
        'test_multiply_bytearray',
        'test_multiply_class',
        'test_multiply_frozenset',
        'test_multiply_list',
        'test_multiply_str',
        'test_multiply_tuple',


        'test_power_class',
        'test_power_frozenset',

        'test_rshift_class',
        'test_rshift_frozenset',

        'test_subtract_class',

        'test_true_divide_class',

        'test_xor_class',
        'test_xor_frozenset',
    ]
