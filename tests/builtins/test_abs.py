from .. utils import TranspileTestCase, BuiltinFunctionTestCase

from unittest import expectedFailure


class AbsTests(TranspileTestCase):
    def test_abs_not_implemented(self):
        self.assertCodeExecution("""
            class NotAbsLike:
                pass
            x = NotAbsLike()
            try:
                print(abs(x))
            except TypeError as err:
                print(err)
            """)

    @expectedFailure
    def test_incorrect_abs_call(self):
        self.assertCodeExecution("""
            x = 1
            print(x.abs())
            """)


class BuiltinAbsFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["abs"]

    not_implemented = [
    ]
