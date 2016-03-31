from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class DivmodTests(TranspileTestCase):
    def test_int_int_zero_rem(self):
        self.assertCodeExecution("""
            x = 4
            y = 2
            print(divmod(x, y))
            print('Done.')
            """)

    def test_int_int_one_rem(self):
        self.assertCodeExecution("""
            x = 7
            y = 3
            print(divmod(x, y))
            print('Done.')
            """)

    def test_int_float(self):
        self.assertCodeExecution("""
            x = 7
            y = 3.3
            print(divmod(x, y))
            print('Done.')
            """)

    def test_int_bool(self):
        self.assertCodeExecution("""
            x = 7
            y = True
            print(divmod(x, y))
            print('Done.')
            """)

    def test_int_list(self):
        self.assertCodeExecution("""
            x = 7
            y = [3, 4]
            print(divmod(x, y))
            print('Done.')
            """)

    def test_int_none(self):
        self.assertCodeExecution("""
            x = 7
            y = None
            print(divmod(x, y))
            print('Done.')
            """)

    def test_int_str(self):
        self.assertCodeExecution("""
            x = 7
            y = 'abc'
            print(divmod(x, y))
            print('Done.')
            """)

    def test_int_str_empty(self):
        self.assertCodeExecution("""
            x = 7
            y = ''
            print(divmod(x, y))
            print('Done.')
            """)

    def test_none_int(self):
        self.assertCodeExecution("""
            x = None
            y = 7
            print(divmod(x, y))
            print('Done.')
            """)

    def test_none_none(self):
        self.assertCodeExecution("""
            x = None
            y = None
            print(divmod(x, y))
            print('Done.')
            """)


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
