from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class IntTests(TranspileTestCase):

    def test_bad_int(self):
        self.assertCodeExecution("""
            try:
                print(int(1, 2, 3))
            except TypeError as err:
                print(err)

            try:
                print(int([1, 2, 3]))
            except TypeError as err:
                print(err)
        """)


class BuiltinIntFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["int"]

    not_implemented = [
        'test_bytearray',
        'test_bytes',
    ]
