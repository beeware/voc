from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class RangeTests(TranspileTestCase):
    def test_creation(self):
        self.assertCodeExecution("""
            x = range(0, 5)
            print("x[0] = ", x[0])
            print("x[1] = ", x[1])
            print("x[3] = ", x[3])
            print("x[-1] = ", x[-1])
            print("x[5] = ", x[5])
            """)

    def test_step(self):
        self.assertCodeExecution("""
            x = range(0, 5, 2)
            print("x[0] = ", x[0])
            print("x[1] = ", x[1])
            print("x[3] = ", x[3])
            print("x[-1] = ", x[-1])
            print("x[5] = ", x[5])
            """)


class UnaryRangeOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'range'

    not_implemented = [
        'test_unary_invert',
        'test_unary_negative',
        'test_unary_not',
        'test_unary_positive',
    ]


class BinaryRangeOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'range'

    not_implemented = [
        'test_add_bytearray',
        'test_add_class',
        'test_add_complex',
        'test_add_frozenset',
        'test_add_slice',

        'test_and_bytearray',
        'test_and_class',
        'test_and_complex',
        'test_and_frozenset',
        'test_and_slice',

        'test_eq_bytearray',
        'test_eq_class',
        'test_eq_complex',
        'test_eq_frozenset',
        'test_eq_range',
        'test_eq_slice',

        'test_floor_divide_bytearray',
        'test_floor_divide_class',
        'test_floor_divide_complex',
        'test_floor_divide_frozenset',
        'test_floor_divide_slice',

        'test_ge_bool',
        'test_ge_bytearray',
        'test_ge_bytes',
        'test_ge_class',
        'test_ge_complex',
        'test_ge_dict',
        'test_ge_float',
        'test_ge_frozenset',
        'test_ge_int',
        'test_ge_list',
        'test_ge_None',
        'test_ge_NotImplemented',
        'test_ge_range',
        'test_ge_set',
        'test_ge_slice',
        'test_ge_str',
        'test_ge_tuple',

        'test_gt_bool',
        'test_gt_bytearray',
        'test_gt_bytes',
        'test_gt_class',
        'test_gt_complex',
        'test_gt_dict',
        'test_gt_float',
        'test_gt_frozenset',
        'test_gt_int',
        'test_gt_list',
        'test_gt_None',
        'test_gt_NotImplemented',
        'test_gt_range',
        'test_gt_set',
        'test_gt_slice',
        'test_gt_str',
        'test_gt_tuple',

        'test_le_bool',
        'test_le_bytearray',
        'test_le_bytes',
        'test_le_class',
        'test_le_complex',
        'test_le_dict',
        'test_le_float',
        'test_le_frozenset',
        'test_le_int',
        'test_le_list',
        'test_le_None',
        'test_le_NotImplemented',
        'test_le_range',
        'test_le_set',
        'test_le_slice',
        'test_le_str',
        'test_le_tuple',

        'test_lshift_bytearray',
        'test_lshift_class',
        'test_lshift_complex',
        'test_lshift_frozenset',
        'test_lshift_slice',

        'test_lt_bool',
        'test_lt_bytearray',
        'test_lt_bytes',
        'test_lt_class',
        'test_lt_complex',
        'test_lt_dict',
        'test_lt_float',
        'test_lt_frozenset',
        'test_lt_int',
        'test_lt_list',
        'test_lt_None',
        'test_lt_NotImplemented',
        'test_lt_range',
        'test_lt_set',
        'test_lt_slice',
        'test_lt_str',
        'test_lt_tuple',

        'test_modulo_bytearray',
        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_frozenset',
        'test_modulo_slice',

        'test_multiply_bytearray',
        'test_multiply_bytes',
        'test_multiply_class',
        'test_multiply_complex',
        'test_multiply_frozenset',
        'test_multiply_list',
        'test_multiply_slice',
        'test_multiply_slice',
        'test_multiply_str',
        'test_multiply_tuple',

        'test_ne_bytearray',
        'test_ne_class',
        'test_ne_complex',
        'test_ne_frozenset',
        'test_ne_range',
        'test_ne_slice',

        'test_or_bytearray',
        'test_or_class',
        'test_or_complex',
        'test_or_frozenset',
        'test_or_slice',

        'test_power_bytearray',
        'test_power_class',
        'test_power_complex',
        'test_power_frozenset',
        'test_power_slice',

        'test_rshift_bytearray',
        'test_rshift_class',
        'test_rshift_complex',
        'test_rshift_frozenset',
        'test_rshift_slice',

        'test_subscr_bool',
        'test_subscr_bytearray',
        'test_subscr_bytes',
        'test_subscr_class',
        'test_subscr_complex',
        'test_subscr_dict',
        'test_subscr_float',
        'test_subscr_frozenset',
        'test_subscr_int',
        'test_subscr_list',
        'test_subscr_None',
        'test_subscr_NotImplemented',
        'test_subscr_range',
        'test_subscr_set',
        'test_subscr_slice',
        'test_subscr_str',
        'test_subscr_tuple',

        'test_subtract_bytearray',
        'test_subtract_class',
        'test_subtract_complex',
        'test_subtract_frozenset',
        'test_subtract_slice',

        'test_true_divide_bytearray',
        'test_true_divide_class',
        'test_true_divide_complex',
        'test_true_divide_frozenset',
        'test_true_divide_slice',

        'test_xor_bytearray',
        'test_xor_class',
        'test_xor_complex',
        'test_xor_frozenset',
        'test_xor_slice',
    ]


class InplaceRangeOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'range'

    not_implemented = [
        'test_add_bytearray',
        'test_add_class',
        'test_add_complex',
        'test_add_frozenset',
        'test_add_slice',

        'test_and_bytearray',
        'test_and_class',
        'test_and_complex',
        'test_and_frozenset',
        'test_and_slice',

        'test_floor_divide_bytearray',
        'test_floor_divide_class',
        'test_floor_divide_complex',
        'test_floor_divide_frozenset',
        'test_floor_divide_slice',

        'test_lshift_bytearray',
        'test_lshift_class',
        'test_lshift_complex',
        'test_lshift_frozenset',
        'test_lshift_slice',

        'test_modulo_bytearray',
        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_frozenset',
        'test_modulo_slice',

        'test_multiply_bytearray',
        'test_multiply_class',
        'test_multiply_complex',
        'test_multiply_frozenset',
        'test_multiply_slice',

        'test_or_bytearray',
        'test_or_class',
        'test_or_complex',
        'test_or_frozenset',
        'test_or_slice',

        'test_power_bytearray',
        'test_power_class',
        'test_power_complex',
        'test_power_frozenset',
        'test_power_slice',

        'test_rshift_bytearray',
        'test_rshift_class',
        'test_rshift_complex',
        'test_rshift_frozenset',
        'test_rshift_slice',

        'test_subtract_bytearray',
        'test_subtract_class',
        'test_subtract_complex',
        'test_subtract_frozenset',
        'test_subtract_slice',

        'test_true_divide_bytearray',
        'test_true_divide_class',
        'test_true_divide_complex',
        'test_true_divide_frozenset',
        'test_true_divide_slice',

        'test_xor_bytearray',
        'test_xor_class',
        'test_xor_complex',
        'test_xor_frozenset',
        'test_xor_slice',
    ]
