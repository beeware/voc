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

    def test_find(self):
        self.assertCodeExecution("""
            print(b''.find(b'a'))
            print(b'abcd'.find(b''))
            print(b'abcd'.find(b'...'))
            print(b'abcd'.find(b'a'))
            print(b'abcd'.find(b'b'))
            print(b'abcd'.find(b'c'))
            print(b'abcd'.find(b'd'))
            print(b'abcd'.find(b'ab'))
            print(b'abcd'.find(b'bc'))
            print(b'abcd'.find(b'cd'))
            print(b'abcd'.find(b'cd', 2))
            print(b'abcd'.find(b'ab', 3))
            print(b'abcd'.find(b'cd', 2, 3))
            print(b'abcd'.find(b'ab', 3, 4))
        """)


class UnaryBytesOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'bytes'

    not_implemented = [
    ]


class BinaryBytesOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'bytes'

    not_implemented = [
        'test_direct_eq_bytearray',
        'test_direct_eq_none',

        'test_direct_ge_bytearray',
        'test_direct_ge_none',

        'test_direct_gt_bytearray',
        'test_direct_gt_none',

        'test_direct_le_bytearray',
        'test_direct_le_none',

        'test_direct_lt_bytearray',
        'test_direct_lt_none',

        'test_direct_ne_bytearray',
        'test_direct_ne_none',

        'test_modulo_complex',
        'test_modulo_dict',
    ]

    not_implemented_versions = {
        'test_modulo_None': (3.5, 3.6),
        'test_modulo_NotImplemented': (3.5, 3.6),
        'test_modulo_bool': (3.5, 3.6),
        'test_modulo_bytearray': (3.5, 3.6),
        'test_modulo_bytes': (3.5, 3.6),
        'test_modulo_class': (3.5, 3.6),
        'test_modulo_float': (3.5, 3.6),
        'test_modulo_frozenset': (3.5, 3.6),
        'test_modulo_int': (3.5, 3.6),
        'test_modulo_list': (3.5, 3.6),
        'test_modulo_range': (3.5, 3.6),
        'test_modulo_set': (3.5, 3.6),
        'test_modulo_slice': (3.5, 3.6),
        'test_modulo_str': (3.5, 3.6),
        'test_modulo_tuple': (3.5, 3.6),
    }

class InplaceBytesOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'bytes'

    not_implemented = [
        'test_modulo_complex',
        'test_modulo_dict',
    ]

    not_implemented_versions = {
        'test_modulo_None': (3.5, 3.6),
        'test_modulo_NotImplemented': (3.5, 3.6),
        'test_modulo_bool': (3.5, 3.6),
        'test_modulo_bytearray': (3.5, 3.6),
        'test_modulo_bytes': (3.5, 3.6),
        'test_modulo_class': (3.5, 3.6),
        'test_modulo_float': (3.5, 3.6),
        'test_modulo_frozenset': (3.5, 3.6),
        'test_modulo_int': (3.5, 3.6),
        'test_modulo_list': (3.5, 3.6),
        'test_modulo_range': (3.5, 3.6),
        'test_modulo_set': (3.5, 3.6),
        'test_modulo_slice': (3.5, 3.6),
        'test_modulo_str': (3.5, 3.6),
        'test_modulo_tuple': (3.5, 3.6),
    }