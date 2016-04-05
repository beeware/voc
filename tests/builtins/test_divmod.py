from .. utils import TranspileTestCase, BuiltinFunctionTestCase, BuiltinTwoargFunctionTestCase


class DivmodTests(TranspileTestCase):
    pass


class BuiltinDivmodFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["divmod"]

    not_implemented = [
        'test_bool',
        'test_bytearray',
        'test_bytes',
        'test_class',
        'test_complex',
        'test_dict',
        'test_float',
        'test_frozenset',
        'test_int',
        'test_list',
        'test_none',
        'test_set',
        'test_str',
        'test_tuple',
    ]


class BuiltinTwoargDivmodFunctionTests(BuiltinTwoargFunctionTestCase, TranspileTestCase):
    functions = ["divmod"]

    not_implemented = [
        'test_bool_bytearray',
        'test_bool_bytes',
        'test_bool_class',
        'test_bool_complex',
        'test_bool_dict',
        'test_bool_frozenset',
        'test_bool_set',
        'test_bytes_bool',
        'test_bytes_bytearray',
        'test_bytes_bytes',
        'test_bytes_class',
        'test_bytes_complex',
        'test_bytes_dict',
        'test_bytes_float',
        'test_bytes_frozenset',
        'test_bytes_int',
        'test_bytes_list',
        'test_bytes_none',
        'test_bytes_set',
        'test_bytes_str',
        'test_bytes_tuple',
        'test_float_bytes',
        'test_int_bytes',
        'test_list_bytes',
        'test_none_bytes',
        'test_str_bytes',
        'test_tuple_bytes',
    ]
