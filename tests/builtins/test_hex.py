from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class HexTests(TranspileTestCase):
    pass


class BuiltinHexFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["hex"]

    not_implemented = [
        'test_bytearray',
        'test_class',
        'test_complex',
        'test_frozenset',
        'test_slice',
    ]
