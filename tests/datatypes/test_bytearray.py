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

    def test_capitalize(self):
        self.assertCodeExecution("""
            print(bytearray(b"abc").capitalize())
            print(bytearray().capitalize())
            """)

    def test_islower(self):
        self.assertCodeExecution("""
            print(bytearray(b'abc').islower())
            print(bytearray(b'').islower())
            print(bytearray(b'Abccc').islower())
            print(bytearray(b'HELLO WORD').islower())
            print(bytearray(b'@#$%!').islower())
            print(bytearray(b'hello world').islower())
            print(bytearray(b'hello world   ').islower())
            # TODO: uncomment when adding support for literal hex bytes
            #print(b'\xf0'.islower())
        """)
        # self.assertCodeExecution("""""")

    def test_upper(self):
        self.assertCodeExecution("""
            print(bytearray(b'abc').upper())
            print(bytearray(b'').upper())
            print(bytearray(b'Abccc').upper())
            print(bytearray(b'HELLO WORD').upper())
            print(bytearray(b'@#$%!').upper())
            print(bytearray(b'hello world').upper())
            print(bytearray(b'hello world   ').upper())
            # TODO: uncomment when adding support for literal hex bytes
            #print(b'\xf0'.upper())
        """)

    def test_isalpha(self):
        self.assertCodeExecution("""
            print(bytearray(b'abc').isalpha())
            print(bytearray(b'').isalpha())
            print(bytearray(b'Abccc').isalpha())
            print(bytearray(b'HELLO WORD').isalpha())
            print(bytearray(b'@#$%!').isalpha())
            print(bytearray(b'hello world').isalpha())
            print(bytearray(b'hello world   ').isalpha())
            # TODO: uncomment when adding support for literal hex bytes
            #print(b'\xf0'.isalpha())
        """)


class UnaryBytearrayOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'bytearray'

    not_implemented = [
    ]


class BinaryBytearrayOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'bytearray'

    not_implemented = [
    ]

    not_implemented_versions = {
        'test_modulo_complex': (3.4, ),
    }


class InplaceBytearrayOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'bytearray'

    not_implemented = [
    ]

    not_implemented_versions = {
        'test_modulo_complex': (3.4, ),
    }
