from .. utils import TranspileTestCase, BuiltinFunctionTestCase, BuiltinTwoargFunctionTestCase


class PowTests(TranspileTestCase):
    def test_int_z(self):
        self.assertCodeExecution("""
            x = 3
            y = 4
            z = 5
            try:
                print(pow(x, y, z))
            except TypeError as err:
                print(err)
        """)

    def test_int_neg_y_pos_z(self):
        self.assertCodeExecution("""
            x = 3
            y = -4
            z = 5
            try:
                print(pow(x, y, z))
            except (TypeError, ValueError) as err:
                print(type(err))
                print(err)
        """)

    def test_int_neg_y_neg_z(self):
        self.assertCodeExecution("""
            x = 3
            y = -4
            z = -5
            try:
                print(pow(x, y, z))
            except (TypeError, ValueError) as err:
                print(type(err))
                print(err)
        """)

    def test_float_x_with_z(self):
        self.assertCodeExecution("""
            x = 3.3
            y = 4
            z = 5
            try:
                print(pow(x, y, z))
            except TypeError as err:
                print(err)
            """)

    def test_float_y_with_z(self):
        self.assertCodeExecution("""
            x = 3
            y = 4.4
            z = 5
            try:
                print(pow(x, y, z))
            except TypeError as err:
                print(err)
            """)

    def test_float(self):
        self.assertCodeExecution("""
            x = 3.3
            y = 4.4
            z = 5.5
            try:
                print(pow(x, y, z))
            except TypeError as err:
                print(err)
        """)

    def test_float_neg_y_with_z(self):
        self.assertCodeExecution("""
            x = 3.3
            y = -4.4
            z = 5.5
            try:
                print(pow(x, y, z))
            except TypeError as err:
                print(err)
        """)


class BuiltinPowFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["pow"]

    not_implemented = [
        'test_bool',
        'test_bytes',
        'test_bytearray',
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


class BuiltinTwoargPowFunctionTests(BuiltinTwoargFunctionTestCase, TranspileTestCase):
    functions = ["pow"]

    not_implemented = [

        'test_bool_class',
        'test_bool_complex',
        'test_bool_frozenset',


        'test_bytes_class',
        'test_bytes_frozenset',

        'test_class_bool',
        'test_class_bytearray',
        'test_class_float',
        'test_class_frozenset',
        'test_class_int',
        'test_class_set',
        'test_class_tuple',

        'test_complex_bool',
        'test_complex_class',
        'test_complex_complex',
        'test_complex_int',
        'test_complex_set',
        'test_complex_tuple',


        'test_float_complex',
        'test_float_float',

        'test_frozenset_bytes',
        'test_frozenset_float',
        'test_frozenset_range',
        'test_frozenset_int',
        'test_frozenset_None',
        'test_frozenset_str',
        'test_frozenset_tuple',

        'test_int_complex',
        'test_int_float',

        'test_list_frozenset',

        'test_None_class',
        'test_None_frozenset',



        'test_set_frozenset',

        'test_slice_class',

        'test_str_frozenset',

    ]
