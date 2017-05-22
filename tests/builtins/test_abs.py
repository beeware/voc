from .. utils import TranspileTestCase, BuiltinFunctionTestCase


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


class BuiltinAbsFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["abs"]

    not_implemented = [
    ]
