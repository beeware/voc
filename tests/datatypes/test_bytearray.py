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

    def test_contains(self):
        self.assertCodeExecution("""
            print(bytearray([1,2,3]) in bytearray([1,2]))
            print(bytearray([1,2]) in bytearray([1,2,3]))
            print(bytearray([1,2,4]) in bytearray([1,2,3]))
            print(bytearray([8,9,0,1]) in bytearray([1,2,3]))
            print(101 in bytearray([1,2,3]))
            print(101 in bytearray([1,2,3,101]))
            print(b'pybee' in bytearray([1,2]))
            print(bytearray([1,2]) in b'pybee')
        """)
        self.assertCodeExecution("""
            try:
                print(300 in bytearray([1,2,3]))
                print("No error raised")
            except ValueError:
                print("Raised a ValueError")
        """)
        self.assertCodeExecution("""
            try:
                print(['b', 'e'] in bytearray([1,2,3]))
                print("No error raised")
            except TypeError:
                print("Raised a TypeError")
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

    def test_upper(self):
        # TODO: add this test when adding support for literal hex bytes
        # print(bytearray(b'\xf0').upper())

        self.assertCodeExecution("""
            print(bytearray(b'abc').upper())
            print(bytearray(b'').upper())
            print(bytearray(b'Abccc').upper())
            print(bytearray(b'HELLO WORD').upper())
            print(bytearray(b'@#$%!').upper())
            print(bytearray(b'hello world').upper())
            print(bytearray(b'hello world   ').upper())
        """)

    def test_isalpha(self):
        # TODO: add this test when adding support for literal hex bytes
        # print(bytearray(b'\xf0').isalpha())

        self.assertCodeExecution("""
            print(bytearray(b'abc').isalpha())
            print(bytearray(b'').isalpha())
            print(bytearray(b'Abccc').isalpha())
            print(bytearray(b'HELLO WORD').isalpha())
            print(bytearray(b'@#$%!').isalpha())
            print(bytearray(b'hello world').isalpha())
            print(bytearray(b'hello world   ').isalpha())
        """)

    def test_isupper(self):
        self.assertCodeExecution("""
            print(bytearray(b'abc').isupper())
            print(bytearray(b'ABC').isupper())
            print(bytearray(b'').isupper())
            print(bytearray(b'Abccc').isupper())
            print(bytearray(b'HELLO WORD').isupper())
            print(bytearray(b'@#$%!').isupper())
            print(bytearray(b'hello world').isupper())
            print(bytearray(b'hello world   ').isupper())
        """)

    def test_lower(self):
        self.assertCodeExecution("""
            print(bytearray(b"abc").lower())
            print(bytearray(b"HELLO WORLD!").lower())
            print(bytearray(b"hElLO wOrLd").lower())
            print(bytearray(b"[Hello] World").lower())
            """)
    def test_count(self):
        self.assertCodeExecution("""
            print(bytearray(b'abcabca').count(97))
            print(bytearray(b'abcabca').count(b'abc'))
            print(bytearray(b'qqq').count(b'q'))
            print(bytearray(b'qqq').count(b'qq'))
            print(bytearray(b'qqq').count(b'qqq'))
            print(bytearray(b'qqq').count(b'qqqq'))
            print(bytearray(b'abcdefgh').count(b'bc',-7, -5))
            print(bytearray(b'abcdefgh').count(b'bc',1, -5))
            print(bytearray(b'abcdefgh').count(b'bc',0, 3))
            print(bytearray(b'abcdefgh').count(b'bc',-7, 500))
            print(bytearray(b'qqaqqbqqqcqqqdqqqqeqqqqf').count(b'qq'),1)
            print(bytearray(b'').count(b'q'),0)
        """)

    def test_center(self):
        self.assertCodeExecution("""
            print(bytearray(b'pybee').center(12))
            print(bytearray(b'pybee').center(13))
            print(bytearray(b'pybee').center(2))
            print(bytearray(b'pybee').center(2, b'a'))
            print(bytearray(b'pybee').center(12, b'a'))
            print(bytearray(b'pybee').center(13, b'a'))
            print(bytearray(b'pybee').center(-5))
            print(bytearray(b'').center(5))
            print(bytearray(b'pybee').center(True, b'a'))
            print(bytearray(b'pybee').center(True, bytearray(b'a')))
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
