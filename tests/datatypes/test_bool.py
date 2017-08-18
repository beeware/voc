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
    ]


class InplaceBoolOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'bool'

    not_implemented = [
        'test_add_complex',

        'test_and_int',

        'test_floor_divide_bool',
        'test_floor_divide_float',
        'test_floor_divide_int',

        'test_modulo_bool',
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

        'test_subtract_complex',

        'test_true_divide_bool',
        'test_true_divide_complex',
        'test_true_divide_float',
        'test_true_divide_int',

        'test_xor_int',
    ]
