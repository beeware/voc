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
        'test_None',
        'test_NotImplemented',
        'test_range',
        'test_set',
        'test_slice',
        'test_str',
        'test_tuple',
    ]


class BuiltinTwoargDivmodFunctionTests(BuiltinTwoargFunctionTestCase, TranspileTestCase):
    functions = ["divmod"]

    not_implemented = [
        'test_bool_complex',
        'test_bytearray_complex',
        'test_bytes_complex',
        'test_class_complex',
        'test_dict_complex',
        'test_float_complex',
        'test_frozenset_complex',
        'test_int_complex',
        'test_list_complex',
        'test_None_complex',
        'test_NotImplemented_complex',
        'test_range_complex',
        'test_set_complex',
        'test_slice_complex',
        'test_str_complex',
        'test_tuple_complex',
    ]
