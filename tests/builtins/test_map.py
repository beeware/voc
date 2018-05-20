from .. utils import TranspileTestCase, BuiltinTwoargFunctionTestCase


class MapTests(TranspileTestCase):
    base_code = """
        iterable = %s
        def testish(x):
            return %s
        it = map(testish, iterable)
        print(it)
        print(next(it))
        print(next(it))
        print(next(it))
        try:
            print(next(it))
        except StopIteration:
            pass
    """

    def test_bool(self):
        self.assertCodeExecution(self.base_code % ("[True, False, True]", "bool(x)"))

    def test_bytearray(self):
        self.assertCodeExecution(self.base_code % ("b'123'", "x"))

    def test_float(self):
        self.assertCodeExecution(self.base_code % ("[3.14, 2.17, 1.0]", "x > 1"))

    def test_int(self):
        self.assertCodeExecution(self.base_code % ("[1, 2, 3]", "x * 2"))


class BuiltinMapFunctionTests(BuiltinTwoargFunctionTestCase, TranspileTestCase):
    functions = ["map"]
