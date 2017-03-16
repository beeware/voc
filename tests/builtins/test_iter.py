from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class IterTests(TranspileTestCase):
    pass


class BuiltinIterFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["iter"]

    not_implemented = [
        'test_bytearray',
        'test_bytes',
        'test_class',
        'test_frozenset',
        'test_range',
        'test_set',
        'test_str',
        'test_tuple',
    ]
