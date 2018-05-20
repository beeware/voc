from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class FrozensetTests(TranspileTestCase):
    pass


class BuiltinFrozensetFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["frozenset"]

    not_implemented = [
        'test_bytes',
        'test_str',
    ]

    is_flakey = [
        'test_dict',
        'test_tuple',
    ]
