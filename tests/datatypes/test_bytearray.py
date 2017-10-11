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
            print(bytearray(b'abc').capitalize())
            print(bytearray().capitalize())
        """)

    def test_islower(self):
        # TODO: add this test when adding support for literal hex bytes
        # print(b'\xf0'.islower())

        self.assertCodeExecution("""
            print(bytearray(b'abc').islower())
            print(bytearray(b'').islower())
            print(bytearray(b'Abccc').islower())
            print(bytearray(b'HELLO WORD').islower())
            print(bytearray(b'@#$%!').islower())
            print(bytearray(b'hello world').islower())
            print(bytearray(b'hello world   ').islower())
        """)
        # self.assertCodeExecution("""""")

    def test_isspace(self):
        self.assertCodeExecution("""
            print(bytearray(b'testupper').isspace())
            print(bytearray(b'test isspace').isspace())
            print(bytearray(b' ').isspace())
            print(bytearray(b'').isspace())
            print(bytearray(b'\x46').isspace())
            print(bytearray(b'   \t\t').isspace())
            print(bytearray(b' \x0b').isspace())
            print(bytearray(b' \f').isspace())
            print(bytearray(b' \\n').isspace())
            print(bytearray(b' \\r').isspace())
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
