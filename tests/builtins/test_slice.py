from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class SliceTests(TranspileTestCase):
    def test_slice_repr_stop(self):
        self.assertCodeExecution("""
            print(slice(0))
            print(slice('foo'))
            """)

    def test_slice_repr_start_stop(self):
        self.assertCodeExecution("""
            print(slice(0, 100))
            print(slice('foo', Exception))
            """)

    def test_slice_repr_start_stop_step(self):
        self.assertCodeExecution("""
            print(slice(0, 100, 2))
            print(slice('foo', Exception, object()))
            """)


class BuiltinSliceFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["slice"]

    not_implemented = [
        'test_class',
        'test_complex',
    ]
