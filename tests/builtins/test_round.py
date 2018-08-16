from .. utils import TranspileTestCase, BuiltinFunctionTestCase, BuiltinTwoargFunctionTestCase


class RoundTests(TranspileTestCase):
    pass


class BuiltinRoundFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["round"]


class BuiltinRoundTwoargFunctionTests(BuiltinTwoargFunctionTestCase, TranspileTestCase):
    functions = ["round"]
    python_types = [
        'None',
        'NotImplemented',
        'bool',
        'bytearray',
        'bytes',
        'class',
        'complex',
        'dict',
        'float',
        'frozenset',
        'int',
        'list',
        'range',
        'set',
        'slice',
        'str',
        'tuple',
        'obj',
    ]

    not_implemented_types = [
        'test_float',
    ]

    not_implemented = [
        'test_bool_bool',
        'test_bool_int',
        'test_int_bool',
        'test_int_int',
    ]

    not_implemented_versions = {
        'test_bool_None': (3.5, 3.6),
        'test_int_None': (3.5, 3.6),
    }

    for not_implemented_type in not_implemented_types:
        for python_type in python_types:
            not_implemented.append('_'.join([not_implemented_type, python_type]))
