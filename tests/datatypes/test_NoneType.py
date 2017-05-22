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





        'test_eq_class',

        'test_ge_class',

        'test_gt_class',

        'test_le_class',


        'test_lt_class',

        'test_modulo_complex',

        'test_multiply_bytes',
        'test_multiply_bytearray',

        'test_ne_class',







    ]


class InplaceNoneTypeOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'None'

    not_implemented = [




        'test_modulo_complex',

        'test_multiply_bytes',
        'test_multiply_bytearray',
        'test_multiply_list',
        'test_multiply_str',
        'test_multiply_tuple',






    ]
