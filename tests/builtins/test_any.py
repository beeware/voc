from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class AnyTests(TranspileTestCase):
    pass


class BuiltinAnyFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["any"]

    not_implemented = [
        'test_bytearray',
        'test_bytes',
        'test_class',
        'test_complex',
        'test_dict',
        'test_frozenset',
        'test_set',
        'test_slice',
        'test_str',
    ]
