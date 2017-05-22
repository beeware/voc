from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class SliceTests(TranspileTestCase):
    def test_slice_list(self):
        self.assertCodeExecution("""
            x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            print("x[:] = ", x[:])
            print("x[5:] = ", x[5:])
            print("x[:5] = ", x[:5])
            print("x[2:8] = ", x[2:8])

            print("x[::2] = ", x[::2])
            print("x[5::2] = ", x[5::2])
            print("x[:5:2] = ", x[:5:2])
            print("x[2:8:2] = ", x[2:8:2])
            """)

    def test_slice_range(self):
        self.assertCodeExecution("""
            x = range(0, 10)
            print("x[:] = ", x[:])
            print("x[5:] = ", x[5:])
            print("x[:5] = ", x[:5])
            print("x[2:8] = ", x[2:8])

            print("x[::2] = ", x[::2])
            print("x[5::2] = ", x[5::2])
            print("x[:5:2] = ", x[:5:2])
            print("x[2:8:2] = ", x[2:8:2])
            """)

    def test_slice_string(self):
        self.assertCodeExecution("""
            x = "0123456789a"
            print("x[:] = ", x[:])
            print("x[5:] = ", x[5:])
            print("x[:5] = ", x[:5])
            print("x[2:8] = ", x[2:8])

            print("x[::2] = ", x[::2])
            print("x[5::2] = ", x[5::2])
            print("x[:5:2] = ", x[:5:2])
            print("x[2:8:2] = ", x[2:8:2])
            """)

    def test_slice_tuple(self):
        self.assertCodeExecution("""
            x = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
            print("x[:] = ", x[:])
            print("x[5:] = ", x[5:])
            print("x[:5] = ", x[:5])
            print("x[2:8] = ", x[2:8])

            print("x[::2] = ", x[::2])
            print("x[5::2] = ", x[5::2])
            print("x[:5:2] = ", x[:5:2])
            print("x[2:8:2] = ", x[2:8:2])
            """)


class UnarySliceOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'slice'

    not_implemented = [
        'test_unary_invert',
        'test_unary_negative',
        'test_unary_not',
        'test_unary_positive',
    ]


class BinarySliceOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'slice'

    not_implemented = [


        'test_direct_ge_frozenset',
        'test_direct_gt_frozenset',

        'test_direct_eq_slice',
        'test_direct_ge_slice',
        'test_direct_gt_slice',
        'test_direct_le_slice',
        'test_direct_lt_slice',
        'test_direct_ne_slice',

        'test_eq_class',
        'test_eq_frozenset',
        'test_eq_slice',

        'test_ge_bytearray',
        'test_ge_class',
        'test_ge_complex',
        'test_ge_dict',
        'test_ge_slice',

        'test_gt_bytearray',
        'test_gt_class',
        'test_gt_dict',
        'test_gt_float',
        'test_gt_frozenset',
        'test_gt_slice',

        'test_le_class',
        'test_le_NotImplemented',
        'test_le_slice',

        'test_lshift_class',

        'test_lt_class',
        'test_lt_int',
        'test_lt_slice',

        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_frozenset',

        'test_multiply_bytearray',
        'test_multiply_bytes',
        'test_multiply_list',
        'test_multiply_str',
        'test_multiply_tuple',

        'test_ne_class',
        'test_ne_slice',




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



    ]


class InplaceSliceOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'slice'

    not_implemented = [



        'test_modulo_complex',

        'test_multiply_bytearray',
        'test_multiply_bytes',
        'test_multiply_class',
        'test_multiply_list',
        'test_multiply_str',
        'test_multiply_tuple',


        'test_power_frozenset',

        'test_rshift_class',


        'test_true_divide_class',

        'test_xor_frozenset',
    ]
