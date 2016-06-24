from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class LenTests(TranspileTestCase):
    pass


class BuiltinLenFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["len"]

    not_implemented = [
        'test_bytearray',
        'test_bytes',
        'test_class',
        'test_complex',
        'test_frozenset',
        'test_range',
        'test_slice',
        'test_tuple',
    ]
