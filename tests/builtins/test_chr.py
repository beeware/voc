from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class ChrTests(TranspileTestCase):
    pass


class BuiltinChrFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["chr"]

    not_implemented = [
        'test_bytearray',
        'test_bytes',
        'test_class',
        'test_complex',
        'test_dict',
        'test_frozenset',
        'test_set',
    ]
