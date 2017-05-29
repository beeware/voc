from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class AllTests(TranspileTestCase):
    pass


class BuiltinAllFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["all"]

    not_implemented = [
        'test_bytearray',
    ]
