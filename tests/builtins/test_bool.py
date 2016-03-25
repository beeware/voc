from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class BoolTests(TranspileTestCase):
    pass


class BuiltinBoolFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["bool"]

    not_implemented = [
        'test_bytearray',
        'test_bytes',
        'test_class',
        'test_complex',
        'test_dict',
        'test_float',
        'test_frozenset',
        'test_list',
        'test_set',
        'test_tuple',
    ]
