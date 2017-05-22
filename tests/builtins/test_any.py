from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class AnyTests(TranspileTestCase):
    pass


class BuiltinAnyFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["any"]

    not_implemented = [
        'test_bytearray',
        'test_class',
        'test_dict',
        'test_frozenset',
        'test_set',
        'test_str',
    ]
