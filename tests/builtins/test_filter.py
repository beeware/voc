from .. utils import TranspileTestCase, BuiltinTwoargFunctionTestCase


class FilterTests(TranspileTestCase):
    pass


class BuiltinFilterFunctionTests(BuiltinTwoargFunctionTestCase, TranspileTestCase):
    functions = ["filter"]

    not_implemented = [
        'test_bool_bool',
        'test_bool_bytes',
        'test_bool_float',
        'test_bool_int',
        'test_bool_list',
        'test_bool_none',
        'test_bool_str',
        'test_bool_tuple',

        'test_bytes_bool',
        'test_bytes_bytes',
        'test_bytes_float',
        'test_bytes_int',
        'test_bytes_list',
        'test_bytes_none',
        'test_bytes_str',
        'test_bytes_tuple',

        'test_float_bool',
        'test_float_bytes',
        'test_float_float',
        'test_float_int',
        'test_float_list',
        'test_float_none',
        'test_float_str',
        'test_float_tuple',

        'test_int_bool',
        'test_int_bytes',
        'test_int_float',
        'test_int_int',
        'test_int_list',
        'test_int_none',
        'test_int_str',
        'test_int_tuple',

        'test_list_bool',
        'test_list_bytes',
        'test_list_float',
        'test_list_int',
        'test_list_list',
        'test_list_none',
        'test_list_str',
        'test_list_tuple',

        'test_none_bool',
        'test_none_bytes',
        'test_none_float',
        'test_none_int',
        'test_none_list',
        'test_none_none',
        'test_none_str',
        'test_none_tuple',

        'test_str_bool',
        'test_str_bytes',
        'test_str_float',
        'test_str_int',
        'test_str_list',
        'test_str_none',
        'test_str_str',
        'test_str_tuple',

        'test_tuple_bool',
        'test_tuple_bytes',
        'test_tuple_float',
        'test_tuple_int',
        'test_tuple_list',
        'test_tuple_none',
        'test_tuple_str',
        'test_tuple_tuple',
    ]
