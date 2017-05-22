from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class SetTests(TranspileTestCase):
    pass


class BuiltinSetFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["set"]

    not_implemented = [
        'test_bytearray',
        'test_bytes',
        'test_class',
        'test_dict',
        'test_str',
        'test_tuple',
    ]
