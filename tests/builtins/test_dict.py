from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class DictTests(TranspileTestCase):
    pass


class BuiltinDictFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["dict"]

    not_implemented = [
        'test_bytearray',
        'test_bytes',
        'test_class',
        'test_complex',
        'test_frozenset',
        'test_list',
        'test_set',
        'test_slice',
        'test_str',
    ]
