from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class RangeTests(TranspileTestCase):
    pass


class BuiltinRangeFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["range"]

    not_implemented = [
        'test_bool',
    ]
