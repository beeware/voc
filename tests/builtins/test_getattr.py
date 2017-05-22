from .. utils import TranspileTestCase, BuiltinTwoargFunctionTestCase


class GetattrTests(TranspileTestCase):
    def test_minimal(self):
        self.assertCodeExecution("""
            class MyClass(object):
                class_value = 42

                def __init__(self, val):
                    self.value = val

                def stuff(self, delta):
                    print("DELTA: ", delta)
                    return self.value + delta

            print("On class: ")
            print('  class_value =', getattr(MyClass, 'class_value'))
            # print('  stuff =', getattr(MyClass, 'stuff'))  # FIXME
            try:
                getattr(MyClass, 'foo')
                print("  Shouldn't be able to get attribute foo")
            except AttributeError:
                print("  Can't get attribute foo")
            print('  foo (default) =', getattr(MyClass, 'foo', 42))

            obj = MyClass(37)

            print("On instance:")
            print('  class_value =', getattr(obj, 'class_value'))
            print('  value =', getattr(obj, 'value'))
            # print('  stuff =', getattr(obj, 'stuff'))  # FIXME
            try:
                getattr(MyClass, 'foo')
                print("  Shouldn't be able to get attribute foo")
            except AttributeError:
                print("  Can't get attribute foo")
            print('  foo (default) =', getattr(obj, 'foo', 42))
            """, run_in_function=False)


class BuiltinGetattrFunctionTests(BuiltinTwoargFunctionTestCase, TranspileTestCase):
    functions = ["getattr"]

    not_implemented = [
        'test_bool_class',
        'test_bool_frozenset',

        'test_bytearray_class',
        'test_bytearray_frozenset',

        'test_bytes_class',
        'test_bytes_frozenset',

        'test_class_bytes',
        'test_class_class',
        'test_class_complex',
        'test_class_dict',
        'test_class_float',
        'test_class_frozenset',
        'test_class_int',
        'test_class_list',
        'test_class_None',
        'test_class_NotImplemented',
        'test_class_range',
        'test_class_set',
        'test_class_slice',
        'test_class_str',

        'test_complex_class',
        'test_complex_frozenset',

        'test_dict_class',
        'test_dict_frozenset',

        'test_float_class',
        'test_float_frozenset',

        'test_frozenset_bool',
        'test_frozenset_bytearray',
        'test_frozenset_bytes',
        'test_frozenset_complex',
        'test_frozenset_dict',
        'test_frozenset_float',
        'test_frozenset_frozenset',
        'test_frozenset_int',
        'test_frozenset_list',
        'test_frozenset_None',
        'test_frozenset_NotImplemented',
        'test_frozenset_slice',
        'test_frozenset_str',
        'test_frozenset_tuple',

        'test_int_frozenset',

        'test_list_class',
        'test_list_frozenset',

        'test_None_class',
        'test_None_frozenset',

        'test_NotImplemented_class',
        'test_NotImplemented_frozenset',

        'test_range_class',
        'test_range_frozenset',

        'test_set_class',
        'test_set_frozenset',

        'test_slice_class',
        'test_slice_frozenset',

        'test_str_class',

        'test_tuple_class',
        'test_tuple_frozenset',
    ]
