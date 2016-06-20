from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class FloatTests(TranspileTestCase):
    pass


class BuiltinFloatFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["float"]

    not_implemented = [
        'test_bytearray',
        'test_bytes',
        'test_class',
        'test_complex',
        'test_frozenset',
        'test_slice',
    ]
