
from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class StrTests(TranspileTestCase):
    def test_setattr(self):
        self.assertCodeExecution("""
            x = "Hello, world"
            x.attr = 42
            print('Done.')
            """)

    def test_endswith(self):
        self.assertCodeExecution("""
            s = "abracadabra"
            suffix = "abra"
            print(s.endswith(end))
            """)

        self.assertCodeExecution("""
            s = "abracadabra"
            suffix = "ABRA"
            print(s.endswith(end))
            """)

        self.assertCodeExecution("""
            s = "ABRACADABRA"
            suffix = "abra"
            print(s.endswith(end))
            """)


        #self.assertCodeExecution("""
        #  print('abracadabra'.endswith('abra'))
        #    """)

    def test_getattr(self):
        self.assertCodeExecution("""
            x = "Hello, world"
            print(x.attr)
            print('Done.')
            """)

    def test_getitem(self):
        # Simple positive index
        self.assertCodeExecution("""
            x = "12345"
            print(x[2])
            """)

        # Simple negative index
        self.assertCodeExecution("""
            x = "12345"
            print(x[-2])
            """)

        # Positive index out of range
        self.assertCodeExecution("""
            x = "12345"
            print(x[10])
            """)

        # Negative index out of range
        self.assertCodeExecution("""
            x = "12345"
            print(x[-10])
            """)

    def test_slice(self):
        # Full slice
        self.assertCodeExecution("""
            x = "12345"
            print(x[:])
            """)

        # Left bound slice
        self.assertCodeExecution("""
            x = "12345"
            print(x[1:])
            """)

        # Right bound slice
        self.assertCodeExecution("""
            x = "12345"
            print(x[:4])
            """)

        # Slice bound in both directions
        self.assertCodeExecution("""
            x = "12345"
            print(x[1:4])
            """)

        # Slice bound in both directions with end out of bounds
        self.assertCodeExecution("""
            x = "12345"
            print(x[1:6])
            """)

        # Slice bound in both directions with start out of bounds
        self.assertCodeExecution("""
            x = "12345"
            print(x[6:7])
            """)

    def test_case_changes(self):
        self.assertCodeExecution("""
            for s in ['hello, world', 'HEllo, WORLD', 'átomo', '']:
                print(s.capitalize())
                print(s.lower())
                # print(s.swap())
                print(s.title())
                print(s.upper())
            """)

    def test_index(self):
        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.index('hell'))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.index('world'))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.index('hell', 1))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.index('hell', 1, 3))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.index('hell', 1, 100))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.index('hell', 1, -1))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.index('hell', -4))
            """)

    def test_count(self):
        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.count('e'))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.count('a'))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.count('ll'))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.count('ll', 3))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.count('ll', 3, 4))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.count('ll', 0, 4))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.count('ll', 0, 100))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.count('hell', 1, -1))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.count('hell', -4))
            """)

    def test_find(self):
        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.find('hell'))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.find('world'))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.find('hell', 1))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.find('hell', 1, 3))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.find('hell', 1, 100))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.find('hell', 1, -1))
            """)

        self.assertCodeExecution("""
            s = 'hello hell'
            print(s.find('hell', -4))
            """)

    def test_expand(self):
        self.assertCodeExecution("""
            print('\\t'.expandtabs())
            print('a\\t'.expandtabs())
            print('aa\\t'.expandtabs())
            print('aaa\\t'.expandtabs())
            print('aaaaaaaa\\t'.expandtabs())
            print('a\\naa\\t'.expandtabs())
            print('\\t'.expandtabs(3))
            print('a\\t'.expandtabs(3))
            print('aa\\t'.expandtabs(7))
            print('aaa\\t'.expandtabs(4))
            print('aaaaaaaa\\t'.expandtabs(4))
            print('a\\naa\\t'.expandtabs(4))
            """)

    def test_title(self):
        self.assertCodeExecution("""
            s = ' foo  bar    baz '
            print(s.title())
        """)

    def test_len(self):
        self.assertCodeExecution("""
            s = ' foo  bar    baz '
            print(len(s))
        """)


class UnaryStrOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'str'

    not_implemented = [
    ]


class BinaryStrOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'str'

    not_implemented = [
        'test_add_class',
        'test_add_frozenset',

        'test_and_class',
        'test_and_frozenset',

        'test_eq_class',
        'test_eq_frozenset',

        'test_floor_divide_class',
        'test_floor_divide_complex',
        'test_floor_divide_frozenset',

        'test_ge_class',
        'test_ge_frozenset',

        'test_gt_class',
        'test_gt_frozenset',

        'test_le_class',
        'test_le_frozenset',

        'test_lshift_class',
        'test_lshift_frozenset',

        'test_lt_class',
        'test_lt_frozenset',

        'test_modulo_bool',
        'test_modulo_bytes',
        'test_modulo_bytearray',
        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_dict',
        'test_modulo_float',
        'test_modulo_frozenset',
        'test_modulo_slice',
        'test_modulo_int',
        'test_modulo_list',
        'test_modulo_None',
        'test_modulo_NotImplemented',
        'test_modulo_range',
        'test_modulo_set',
        'test_modulo_str',
        'test_modulo_tuple',

        'test_multiply_class',
        'test_multiply_frozenset',

        'test_ne_class',
        'test_ne_frozenset',

        'test_or_class',
        'test_or_frozenset',

        'test_power_class',
        'test_power_frozenset',

        'test_rshift_class',
        'test_rshift_frozenset',

        'test_subscr_bool',
        'test_subscr_class',
        'test_subscr_frozenset',
        'test_subscr_slice',

        'test_subtract_class',
        'test_subtract_frozenset',

        'test_true_divide_class',
        'test_true_divide_frozenset',

        'test_xor_class',
        'test_xor_frozenset',
    ]


class InplaceStrOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'str'

    not_implemented = [
        'test_add_class',
        'test_add_frozenset',

        'test_and_class',
        'test_and_frozenset',

        'test_floor_divide_class',
        'test_floor_divide_complex',
        'test_floor_divide_frozenset',

        'test_lshift_class',
        'test_lshift_frozenset',

        'test_modulo_bool',
        'test_modulo_bytes',
        'test_modulo_bytearray',
        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_dict',
        'test_modulo_float',
        'test_modulo_frozenset',
        'test_modulo_slice',
        'test_modulo_int',
        'test_modulo_list',
        'test_modulo_None',
        'test_modulo_NotImplemented',
        'test_modulo_range',
        'test_modulo_set',
        'test_modulo_str',
        'test_modulo_tuple',

        'test_multiply_class',
        'test_multiply_frozenset',

        'test_or_class',
        'test_or_frozenset',

        'test_power_class',
        'test_power_frozenset',

        'test_rshift_class',
        'test_rshift_frozenset',

        'test_subtract_class',
        'test_subtract_frozenset',

        'test_true_divide_class',
        'test_true_divide_frozenset',

        'test_xor_class',
        'test_xor_frozenset',
    ]
