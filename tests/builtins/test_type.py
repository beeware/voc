from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class TypeTests(TranspileTestCase):
    pass


class BuiltinTypeFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["type"]

    not_implemented = [
        'test_bytearray',
        'test_class',
        'test_complex',
        'test_frozenset',
        'test_slice',
    ]
