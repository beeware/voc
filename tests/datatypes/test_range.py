from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class RangeTests(TranspileTestCase):
    def test_creation(self):
        self.assertCodeExecution("""
            x = range(0, 5)
            print("x[0] = ", x[0])
            print("x[1] = ", x[1])
            print("x[3] = ", x[3])
            print("x[-1] = ", x[-1])
            try:
                print("x[5] = ", x[5])
            except IndexError as err:
                print(err)
            """)

    def test_step(self):
        self.assertCodeExecution("""
            x = range(0, 5, 2)
            print("x[0] = ", x[0])
            print("x[1] = ", x[1])
            print("x[-1] = ", x[-1])
            print("x[-3] = ", x[-3])
            try:
                print("x[3] = ", x[3])
            except IndexError as err:
                print(err)
            try:
                print("x[5] = ", x[5])
            except IndexError as err:
                print(err)
            try:
                print("x[-4] = ", x[-4])
            except IndexError as err:
                print(err)

            y = range(7, 1, -3)
            print("y[0] = ", y[0])
            print("y[1] = ", y[1])
            print("y[-2] = ", y[-2])
            """)

    def test_zero_step(self):
        self.assertCodeExecution("""
            try:
                range(0, 5, 0)
            except ValueError as err:
                print(err)
        """)

    def test_len_empty(self):
        self.assertCodeExecution("""
            print(len(range(5, 5)))
        """)

    def test_len_positive_step(self):
        self.assertCodeExecution("""
            print(len(range(5, 0, 1)))
        """)

    def test_len_negative_step(self):
        self.assertCodeExecution("""
            print(len(range(0, 5, -1)))
        """)

    def test_multiple_iterators(self):
        self.assertCodeExecution("""
            r = range(0, 10)
            print(list(r))
            print(list(r))
        """)

    def test_iterator_iterator(self):
        self.assertCodeExecution("""
            r = range(0, 10)
            i = iter(r)
            print(next(i))
            print(next(iter(i)))
            print(r)
        """)


class UnaryRangeOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'range'


class BinaryRangeOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'range'

    not_implemented = [
        'test_add_class',
        'test_add_frozenset',

        'test_and_class',
        'test_and_frozenset',

        'test_direct_eq_frozenset',
        'test_direct_ge_frozenset',
        'test_direct_gt_frozenset',
        'test_direct_le_frozenset',
        'test_direct_lt_frozenset',
        'test_direct_ne_frozenset',

        'test_direct_eq_range',
        'test_direct_ne_range',

        'test_eq_frozenset',
        'test_eq_range',

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

        'test_lshift_class',
        'test_lshift_frozenset',

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

        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_frozenset',

        'test_multiply_bytearray',
        'test_multiply_bytes',
        'test_multiply_class',
        'test_multiply_frozenset',
        'test_multiply_list',
        'test_multiply_str',
        'test_multiply_tuple',

        'test_ne_frozenset',
        'test_ne_range',

        'test_or_class',
        'test_or_frozenset',

        'test_power_class',
        'test_power_frozenset',

        'test_rshift_class',
        'test_rshift_frozenset',

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

        'test_subtract_class',
        'test_subtract_frozenset',

        'test_true_divide_class',
        'test_true_divide_frozenset',

        'test_xor_class',
        'test_xor_frozenset',
    ]


class InplaceRangeOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'range'

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

        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_frozenset',

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
