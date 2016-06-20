from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class RangeTests(TranspileTestCase):
    pass


class BuiltinRangeFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["range"]

    not_implemented = [
        'test_bool',
        'test_bytearray',
        'test_class',
        'test_complex',
        'test_frozenset',
        'test_slice',
    ]
