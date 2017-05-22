from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class IntTests(TranspileTestCase):
    pass


class BuiltinIntFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["int"]

    not_implemented = [
        'test_bytearray',
        'test_bytes',
    ]
