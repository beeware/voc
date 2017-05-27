from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class FrozensetTests(TranspileTestCase):
    pass


class BuiltinFrozensetFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["frozenset"]

    not_implemented = [
        'test_bytearray',
        'test_bytes',
        'test_dict',
        'test_str',
    ]

    not_implemented_versions = {
        'test_tuple': (3.4,),
    }
