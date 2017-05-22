from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase

from unittest import expectedFailure


class BytesTests(TranspileTestCase):
    def test_setattr(self):
        self.assertCodeExecution("""
            x = b'hello, world'
            try:
                x.attr = 42
            except AttributeError as err:
                print(err)
            """)

    def test_getattr(self):
        self.assertCodeExecution("""
            x = b'hello, world'
            try:
                print(x.attr)
            except AttributeError as err:
                print(err)
            """)

    def test_capitalize(self):
        self.assertCodeExecution("""
            print(b'hello, world'.capitalize())
            print(b'helloWORLD'.capitalize())
            print(b'HELLO WORLD'.capitalize())
            print(b'2015638687'.capitalize())
        """)

    @expectedFailure
    def test_capitalize_with_nonascii(self):
        # Move this to test_capitalize upon resolution of #530
        self.assertCodeExecution("""
            print(b'\xc8'.capitalize())
        """)

    def test_iter(self):
        self.assertCodeExecution("""
            print([b for b in b''])
            print([b for b in b'hello world'])
        """)


class UnaryBytesOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'bytes'

    not_implemented = [
    ]


class BinaryBytesOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'bytes'

    not_implemented = [
        'test_add_frozenset',

        'test_and_class',
        'test_and_frozenset',

        'test_direct_eq_bytearray',
        'test_direct_eq_bytes',
        'test_direct_eq_int',
        'test_direct_eq_none',
        'test_direct_eq_set',

        'test_direct_ge_bytearray',
        'test_direct_ge_frozenset',
        'test_direct_ge_none',

        'test_direct_gt_bytearray',
        'test_direct_gt_int',
        'test_direct_gt_none',
        'test_direct_gt_set',
        'test_direct_gt_str',

        'test_direct_le_bytearray',
        'test_direct_le_class',
        'test_direct_le_complex',
        'test_direct_le_none',

        'test_direct_lt_bytearray',
        'test_direct_lt_complex',
        'test_direct_lt_none',

        'test_direct_ne_bytearray',
        'test_direct_ne_bytes',
        'test_direct_ne_complex',
        'test_direct_ne_frozenset',
        'test_direct_ne_list',
        'test_direct_ne_none',
        'test_direct_ne_tuple',

        'test_direct_ge_frozenset',
        'test_direct_ne_frozenset',

        'test_eq_bytearray',
        'test_eq_class',

        'test_ne_class',

        'test_ge_class',

        'test_gt_class',

        'test_le_class',

        'test_lt_class',

        'test_lshift_class',

        'test_modulo_complex',
        'test_modulo_dict',
        'test_modulo_int',


        'test_or_class',


        'test_rshift_frozenset',




    ]


class InplaceBytesOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'bytes'

    not_implemented = [

        'test_and_class',
        'test_and_frozenset',

        'test_floor_divide_class',

        'test_lshift_class',

        'test_modulo_None',
        'test_modulo_complex',
        'test_modulo_dict',
        'test_modulo_list',
        'test_modulo_range',




        'test_rshift_frozenset',



    ]
