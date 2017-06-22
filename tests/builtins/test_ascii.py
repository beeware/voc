import unittest

from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class AsciiTests(TranspileTestCase):
    pass


class BuiltinAsciiFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["ascii"]

    not_implemented = [
        'test_class',
        'test_complex',
    ]

    def test_latin_1(self):
        self.assertCodeExecution("""
            print(ascii('Piñata'))
            """)

    def test_bmp(self):
        self.assertCodeExecution("""
            print(ascii('リュウ・イーユー'))
            """)

    @unittest.expectedFailure
    def test_fake_surrogates(self):
        self.assertCodeExecution(r"""
            print(ascii('\ud801\udc37'))
            """)
