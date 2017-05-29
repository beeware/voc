from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class AnyTests(TranspileTestCase):
    pass


class BuiltinAnyFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["any"]

    not_implemented = [
        'test_bytearray',
    ]
