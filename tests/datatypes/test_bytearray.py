from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class BytearrayTests(TranspileTestCase):
    def test_setattr(self):
        self.assertCodeExecution("""
            x = bytearray([1,2,3])
            try:
                x.attr = 42
            except AttributeError as err:
                print(err)
            """)

    def test_getattr(self):
        self.assertCodeExecution("""
            x = bytearray([1,2,3])
            try:
                print(x.attr)
            except AttributeError as err:
                print(err)
            """)


class UnaryBytearrayOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'bytearray'

    not_implemented = [
    ]


class BinaryBytearrayOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'bytearray'

    not_implemented = [


        'test_direct_eq_frozenset',
        'test_direct_ne_frozenset',

        'test_eq_class',

        'test_ge_class',

        'test_gt_class',

        'test_le_class',
        'test_le_frozenset',


        'test_lt_class',

        'test_modulo_class',
        'test_modulo_complex',


        'test_ne_class',

        'test_or_frozenset',

        'test_power_class',
        'test_power_frozenset',




        'test_true_divide_frozenset',

        'test_xor_class',
    ]


class InplaceBytearrayOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'bytearray'

    not_implemented = [
        'test_add_class',

        'test_and_class',
        'test_and_frozenset',

        'test_floor_divide_class',


        'test_modulo_complex',



        'test_power_class',


        'test_subtract_class',

        'test_true_divide_frozenset',

    ]
