from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class StrTests(TranspileTestCase):
    def test_setattr(self):
        self.assertCodeExecution("""
            x = "Hello, world"
            x.attr = 42
            print('Done.')
            """)

    def test_getattr(self):
        self.assertCodeExecution("""
            x = "Hello, world"
            print(x.attr)
            print('Done.')
            """)

    def test_getitem(self):
        # Simple positive index
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print(x[2])
            """)

        # Simple negative index
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print(x[-2])
            """)

        # Positive index out of range
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print(x[10])
            """)

        # Negative index out of range
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print(x[-10])
            """)

    def test_slice(self):
        # Full slice
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print(x[:])
            """)

        # Left bound slice
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print(x[1:])
            """)

        # Right bound slice
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print(x[:4])
            """)

        # Slice bound in both directions
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print(x[1:4])
            """)


class UnaryStrOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'str'

    not_implemented = [
    ]


class BinaryStrOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'str'

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
        'test_eq_slice',

        'test_floor_divide_bytearray',
        'test_floor_divide_class',
        'test_floor_divide_complex',
        'test_floor_divide_frozenset',
        'test_floor_divide_slice',

        'test_ge_bytearray',
        'test_ge_class',
        'test_ge_complex',
        'test_ge_frozenset',
        'test_ge_slice',

        'test_gt_bytearray',
        'test_gt_class',
        'test_gt_complex',
        'test_gt_frozenset',
        'test_gt_slice',

        'test_le_bytearray',
        'test_le_class',
        'test_le_complex',
        'test_le_frozenset',
        'test_le_slice',

        'test_lshift_bytearray',
        'test_lshift_class',
        'test_lshift_complex',
        'test_lshift_frozenset',
        'test_lshift_slice',

        'test_lt_bytearray',
        'test_lt_class',
        'test_lt_complex',
        'test_lt_frozenset',
        'test_lt_slice',

        'test_modulo_bool',
        'test_modulo_bytes',
        'test_modulo_bytearray',
        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_dict',
        'test_modulo_float',
        'test_modulo_frozenset',
        'test_modulo_slice',
        'test_modulo_int',
        'test_modulo_list',
        'test_modulo_None',
        'test_modulo_NotImplemented',
        'test_modulo_range',
        'test_modulo_set',
        'test_modulo_str',
        'test_modulo_tuple',

        'test_multiply_bytearray',
        'test_multiply_class',
        'test_multiply_complex',
        'test_multiply_frozenset',
        'test_multiply_slice',

        'test_ne_bytearray',
        'test_ne_class',
        'test_ne_complex',
        'test_ne_frozenset',
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

        'test_subscr_bytearray',
        'test_subscr_bytes',
        'test_subscr_class',
        'test_subscr_complex',
        'test_subscr_dict',
        'test_subscr_float',
        'test_subscr_frozenset',
        'test_subscr_slice',
        'test_subscr_list',
        'test_subscr_None',
        'test_subscr_NotImplemented',
        'test_subscr_range',
        'test_subscr_set',
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


class InplaceStrOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'str'

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

        'test_modulo_bool',
        'test_modulo_bytes',
        'test_modulo_bytearray',
        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_dict',
        'test_modulo_float',
        'test_modulo_frozenset',
        'test_modulo_slice',
        'test_modulo_int',
        'test_modulo_list',
        'test_modulo_None',
        'test_modulo_NotImplemented',
        'test_modulo_range',
        'test_modulo_set',
        'test_modulo_str',
        'test_modulo_tuple',

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
