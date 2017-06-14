from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class BoolTests(TranspileTestCase):

    def test_setattr(self):
        self.assertCodeExecution("""
            x = True
            try:
                x.attr = 42
            except AttributeError as err:
                print(err)
            """)

    def test_getattr(self):
        self.assertCodeExecution("""
            x = True
            try:
                print(x.attr)
            except AttributeError as err:
                print(err)
            """)


class UnaryBoolOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'bool'

    not_implemented = [
    ]


class BinaryBoolOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'bool'

    not_implemented = [
        'test_add_complex',
        'test_modulo_complex',
        'test_multiply_complex',
        'test_power_complex',

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

        'test_subtract_complex',

        'test_true_divide_bytearray',
        'test_true_divide_bytes',
        'test_true_divide_class',
        'test_true_divide_complex',
        'test_true_divide_dict',
        'test_true_divide_frozenset',
        'test_true_divide_list',
        'test_true_divide_None',
        'test_true_divide_NotImplemented',
        'test_true_divide_range',
        'test_true_divide_set',
        'test_true_divide_slice',
        'test_true_divide_str',
        'test_true_divide_tuple',

    ]


class InplaceBoolOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'bool'

    not_implemented = [
        'test_add_complex',
        'test_add_float',

        'test_and_int',

        'test_floor_divide_bool',
        'test_floor_divide_float',
        'test_floor_divide_int',

        'test_modulo_bool',
        'test_modulo_complex',
        'test_modulo_float',
        'test_modulo_int',

        'test_multiply_bool',
        'test_multiply_bytearray',
        'test_multiply_bytes',
        'test_multiply_complex',
        'test_multiply_float',
        'test_multiply_int',
        'test_multiply_list',
        'test_multiply_str',
        'test_multiply_tuple',

        'test_or_int',

        'test_power_bool',
        'test_power_complex',
        'test_power_float',
        'test_power_int',

        'test_subtract_bool',
        'test_subtract_complex',
        'test_subtract_float',
        'test_subtract_int',

        'test_true_divide_bool',
        'test_true_divide_complex',
        'test_true_divide_float',
        'test_true_divide_int',

        'test_xor_int',
    ]
