from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class OrdTests(TranspileTestCase):
    pass


class BuiltinOrdFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["ord"]

    not_implemented = [
        'test_bytes',
        'test_bytearray',
    ]
