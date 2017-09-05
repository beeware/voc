from .. utils import TranspileTestCase, BuiltinTwoargFunctionTestCase


class FilterTests(TranspileTestCase):

    def test_bool(self):
        self.assertCodeExecution('print(list(filter(bool, [True, False, True])))')
        self.assertCodeExecution('print(list(filter(bool, [1, 0, 3, -1])))')
        self.assertCodeExecution('print(list(filter(bool, [])))')

    def test_none(self):
        self.assertCodeExecution('print(list(filter(None, [True, False, True])))')
        self.assertCodeExecution('print(list(filter(None, [])))')

    def test_lambda(self):
        self.assertCodeExecution('print(list(filter(lambda x: x > 1, [3, 4, 56, 1, -11])))')

    def test_wrong_argument(self):
        self.assertCodeExecution('print(list(filter(None, None)))', exits_early=True)


class BuiltinFilterFunctionTests(BuiltinTwoargFunctionTestCase, TranspileTestCase):
    functions = ["filter"]

    not_implemented = [
        'test_bool_bytearray',
        'test_bool_bytes',
        'test_bool_dict',
        'test_bool_frozenset',
        'test_bool_list',
        'test_bool_range',
        'test_bool_set',
        'test_bool_str',
        'test_bool_tuple',

        'test_bytearray_bytearray',
        'test_bytearray_bytes',
        'test_bytearray_dict',
        'test_bytearray_frozenset',
        'test_bytearray_list',
        'test_bytearray_range',
        'test_bytearray_set',
        'test_bytearray_str',
        'test_bytearray_tuple',

        'test_bytes_bytearray',
        'test_bytes_bytes',
        'test_bytes_dict',
        'test_bytes_frozenset',
        'test_bytes_list',
        'test_bytes_range',
        'test_bytes_set',
        'test_bytes_str',
        'test_bytes_tuple',

        'test_complex_bytearray',
        'test_complex_bytes',
        'test_complex_dict',
        'test_complex_frozenset',
        'test_complex_list',
        'test_complex_range',
        'test_complex_set',
        'test_complex_str',
        'test_complex_tuple',

        'test_dict_bytearray',
        'test_dict_bytes',
        'test_dict_dict',
        'test_dict_frozenset',
        'test_dict_list',
        'test_dict_range',
        'test_dict_set',
        'test_dict_str',
        'test_dict_tuple',

        'test_float_bytearray',
        'test_float_bytes',
        'test_float_dict',
        'test_float_frozenset',
        'test_float_list',
        'test_float_range',
        'test_float_set',
        'test_float_str',
        'test_float_tuple',

        'test_frozenset_bytearray',
        'test_frozenset_bytes',
        'test_frozenset_dict',
        'test_frozenset_frozenset',
        'test_frozenset_list',
        'test_frozenset_range',
        'test_frozenset_set',
        'test_frozenset_str',
        'test_frozenset_tuple',

        'test_int_bytearray',
        'test_int_bytes',
        'test_int_dict',
        'test_int_frozenset',
        'test_int_list',
        'test_int_range',
        'test_int_set',
        'test_int_str',
        'test_int_tuple',

        'test_list_bytearray',
        'test_list_bytes',
        'test_list_dict',
        'test_list_frozenset',
        'test_list_list',
        'test_list_range',
        'test_list_set',
        'test_list_str',
        'test_list_tuple',

        'test_NotImplemented_bytearray',
        'test_NotImplemented_bytes',
        'test_NotImplemented_dict',
        'test_NotImplemented_frozenset',
        'test_NotImplemented_list',
        'test_NotImplemented_range',
        'test_NotImplemented_set',
        'test_NotImplemented_str',
        'test_NotImplemented_tuple',

        'test_range_bytearray',
        'test_range_bytes',
        'test_range_dict',
        'test_range_frozenset',
        'test_range_list',
        'test_range_range',
        'test_range_set',
        'test_range_str',
        'test_range_tuple',

        'test_set_bytearray',
        'test_set_bytes',
        'test_set_dict',
        'test_set_frozenset',
        'test_set_list',
        'test_set_range',
        'test_set_set',
        'test_set_str',
        'test_set_tuple',

        'test_slice_bytearray',
        'test_slice_bytes',
        'test_slice_dict',
        'test_slice_frozenset',
        'test_slice_list',
        'test_slice_range',
        'test_slice_set',
        'test_slice_str',
        'test_slice_tuple',

        'test_str_bytearray',
        'test_str_bytes',
        'test_str_dict',
        'test_str_frozenset',
        'test_str_list',
        'test_str_range',
        'test_str_set',
        'test_str_str',
        'test_str_tuple',

        'test_tuple_bytearray',
        'test_tuple_bytes',
        'test_tuple_dict',
        'test_tuple_frozenset',
        'test_tuple_list',
        'test_tuple_range',
        'test_tuple_set',
        'test_tuple_str',
        'test_tuple_tuple',
    ]
