from .. utils import TranspileTestCase, BuiltinTwoargFunctionTestCase


class MapTests(TranspileTestCase):
    base_code = """
        iterable = %s
        def testish(x):
            return %s
        it = map(testish, iterable)
        print(it)
        print(next(it))
        print(next(it))
        print(next(it))
        try:
            print(next(it))
        except StopIteration:
            pass
    """

    def test_bool(self):
        self.assertCodeExecution(self.base_code % ("[True, False, True]", "bool(x)"))

    def test_bytearray(self):
        self.assertCodeExecution(self.base_code % ("b'123'", "x"))

    def test_float(self):
        self.assertCodeExecution(self.base_code % ("[3.14, 2.17, 1.0]", "x > 1"))

    def test_int(self):
        self.assertCodeExecution(self.base_code % ("[1, 2, 3]", "x * 2"))


class BuiltinMapFunctionTests(BuiltinTwoargFunctionTestCase, TranspileTestCase):
    functions = ["map"]

    not_implemented = [
        'test_bool_bytearray',
        'test_bool_str',

        'test_bytearray_bytearray',
        'test_bytearray_bytes',
        'test_bytearray_dict',
        'test_bytearray_frozenset',
        'test_bytearray_set',
        'test_bytearray_str',

        'test_bytes_bytearray',
        'test_bytes_dict',
        'test_bytes_set',

        'test_class_bytearray',
        'test_class_class',
        'test_class_dict',
        'test_class_float',
        'test_class_frozenset',
        'test_class_int',
        'test_class_None',
        'test_class_range',
        'test_class_slice',
        'test_class_tuple',

        'test_complex_bytearray',
        'test_complex_bytes',
        'test_complex_class',
        'test_complex_dict',
        'test_complex_set',
        'test_complex_str',

        'test_dict_bytearray',
        'test_dict_class',
        'test_dict_str',

        'test_float_bytearray',
        'test_float_bytes',
        'test_float_class',
        'test_float_dict',
        'test_float_frozenset',
        'test_float_str',

        'test_frozenset_bool',
        'test_frozenset_bytearray',
        'test_frozenset_class',
        'test_frozenset_int',
        'test_frozenset_list',
        'test_frozenset_None',
        'test_frozenset_NotImplemented',
        'test_frozenset_set',
        'test_frozenset_tuple',

        'test_int_bytearray',
        'test_int_class',
        'test_int_str',

        'test_list_bytearray',
        'test_list_bytes',
        'test_list_class',
        'test_list_dict',
        'test_list_frozenset',

        'test_None_bytearray',
        'test_None_bytes',
        'test_None_class',
        'test_None_frozenset',
        'test_None_set',
        'test_None_str',

        'test_NotImplemented_bytearray',
        'test_NotImplemented_class',
        'test_NotImplemented_str',

        'test_range_bytearray',
        'test_range_dict',

        'test_set_bytearray',
        'test_set_bytes',
        'test_set_class',
        'test_set_set',

        'test_slice_bytearray',
        'test_slice_bytes',
        'test_slice_class',
        'test_slice_dict',
        'test_slice_frozenset',
        'test_slice_set',
        'test_slice_str',

        'test_str_bytearray',
        'test_str_dict',
        'test_str_frozenset',
        'test_str_set',
        'test_str_str',

        'test_tuple_bytearray',
        'test_tuple_bytes',
        'test_tuple_dict',
        'test_tuple_frozenset',
        'test_tuple_set',
        'test_tuple_str',
    ]
