from .. utils import TranspileTestCase, BuiltinTwoargFunctionTestCase


class DelattrTests(TranspileTestCase):
    def test_minimal(self):
        self.assertCodeExecution("""
            class MyClass(object):
                class_value = 42

                def __init__(self, val):
                    self.value = val

            print("On class: ")
            delattr(MyClass, 'class_value')
            try:
                print('  class_value =', MyClass.class_value)
                print("  Shouldn't be able to get attribute class_value")
            except AttributeError:
                print("  Can't get attribute class_value")

            try:
                delattr(MyClass, 'class_value')
                print("  Shouldn't be able to delete attribute class_value")
            except AttributeError:
                print("  Can't delete attribute class_value")

            try:
                delattr(MyClass, 'other_class_value')
                print("  Shouldn't be able to delete attribute other_class_value")
            except AttributeError:
                print("  Can't delete attribute other_class_value")

            obj = MyClass(37)

            print("On instance:")
            delattr(obj, 'value')
            try:
                print('  value =', MyClass.value)
                print("  Shouldn't be able to get attribute value")
            except AttributeError:
                print("  Can't get attribute value")

            try:
                delattr(obj, 'value')
                print("  Shouldn't be able to delete attribute value")
            except AttributeError:
                print("  Can't delete attribute value")

            try:
                delattr(obj, 'other_value')
                print("  Shouldn't be able to delete attribute other_value")
            except AttributeError:
                print("  Can't delete attribute other_value")
            """, run_in_function=False)


class BuiltinDelattrFunctionTests(BuiltinTwoargFunctionTestCase, TranspileTestCase):
    functions = ["delattr"]

    not_implemented = [
        'test_bool_frozenset',


        'test_bytes_class',
        'test_bytes_frozenset',

        'test_class_bool',
        'test_class_bytearray',
        'test_class_complex',
        'test_class_dict',
        'test_class_float',
        'test_class_frozenset',
        'test_class_list',
        'test_class_None',
        'test_class_slice',
        'test_class_str',

        'test_complex_class',
        'test_complex_frozenset',

        'test_dict_frozenset',

        'test_float_class',

        'test_frozenset_bytes',
        'test_frozenset_class',
        'test_frozenset_complex',
        'test_frozenset_list',
        'test_frozenset_None',
        'test_frozenset_NotImplemented',
        'test_frozenset_range',
        'test_frozenset_set',
        'test_frozenset_slice',
        'test_frozenset_str',
        'test_frozenset_tuple',

        'test_int_frozenset',

        'test_list_class',
        'test_list_frozenset',

        'test_None_frozenset',

        'test_NotImplemented_frozenset',

        'test_range_class',
        'test_range_frozenset',

        'test_set_frozenset',

        'test_slice_class',

        'test_str_class',

        'test_tuple_class',
        'test_tuple_frozenset',
    ]
