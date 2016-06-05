from .. utils import TranspileTestCase, BuiltinTwoargFunctionTestCase


class FilterTests(TranspileTestCase):
    pass


class BuiltinFilterFunctionTests(BuiltinTwoargFunctionTestCase, TranspileTestCase):
    functions = ["filter"]

    not_implemented = [
        'test_bool_bytes',
        'test_bool_list',
        'test_bool_str',
        'test_bool_tuple',

        'test_bytes_bytes',
        'test_bytes_list',
        'test_bytes_str',
        'test_bytes_tuple',

        'test_float_bytes',
        'test_float_list',
        'test_float_str',
        'test_float_tuple',

        'test_int_bytes',
        'test_int_list',
        'test_int_str',
        'test_int_tuple',

        'test_list_bytes',
        'test_list_list',
        'test_list_str',
        'test_list_tuple',

        'test_none_bytes',
        'test_none_list',
        'test_none_str',
        'test_none_tuple',

        'test_str_bytes',
        'test_str_list',
        'test_str_str',
        'test_str_tuple',

        'test_tuple_bytes',
        'test_tuple_list',
        'test_tuple_str',
        'test_tuple_tuple',
    ]
