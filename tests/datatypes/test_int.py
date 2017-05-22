from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase

from unittest import expectedFailure


class IntTests(TranspileTestCase):
    def test_setattr(self):
        self.assertCodeExecution("""
            x = 37
            try:
                x.attr = 42
            except AttributeError as err:
                print(err)
            """)

    def test_getattr(self):
        self.assertCodeExecution("""
            x = 37
            try:
                print(x.attr)
            except AttributeError as err:
                print(err)
            """)

    @expectedFailure
    def test_invalid_literal(self):
        self.assertCodeExecution("""
            int('q', 16)
            """)


class UnaryIntOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'int'


class BinaryIntOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'int'

    not_implemented = [




        'test_eq_class',

        'test_ge_class',

        'test_gt_class',

        'test_le_class',


        'test_lt_class',

        'test_modulo_complex',

        'test_multiply_complex',

        'test_ne_class',


        'test_power_complex',
        'test_power_float',




        'test_true_divide_complex',

    ]


class InplaceIntOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'int'

    not_implemented = [
        'test_add_complex',


        'test_floor_divide_float',


        'test_modulo_complex',
        'test_modulo_float',

        'test_multiply_bytearray',
        'test_multiply_bytes',
        'test_multiply_complex',
        'test_multiply_float',
        'test_multiply_list',
        'test_multiply_str',
        'test_multiply_tuple',


        'test_power_complex',
        'test_power_float',
        'test_power_int',


        'test_subtract_complex',
        'test_subtract_float',

        'test_true_divide_complex',

    ]
