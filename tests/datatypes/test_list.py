from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class ListTests(TranspileTestCase):
    def test_setattr(self):
        self.assertCodeExecution("""
            x = [1, 2, 3]
            x.attr = 42
            print('Done.')
            """)

    def test_getattr(self):
        self.assertCodeExecution("""
            x = [1, 2, 3]
            print(x.attr)
            print('Done.')
            """)

    def test_creation(self):
        # Empty list
        self.assertCodeExecution("""
            x = []
            print(x)
            """)

        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print(x)
            """)

    def test_getitem(self):
        # Simple positive index
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print(x[2])
            """)

        # Simple negative index
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print(x[-2])
            """)

        # Positive index out of range
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print(x[10])
            """)

        # Negative index out of range
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print(x[-10])
            """)

    def test_setitem(self):
        self.assertCodeExecution("""
            x = [1]
            x[0] = 5
            print(x[0])
            """)

        self.assertCodeExecution("""
            x = [1, 2, 3]
            x[1] = "hello"
            x[2] = "there"
            print(x)
            """)

        # Out of bounds
        self.assertCodeExecution("""
            x = []
            x[0] = 5
            """)

        # Out of bounds (negative)
        self.assertCodeExecution("""
            x = [1]
            x[-2] = 5
            """)

    def test_append(self):
        # New list
        self.assertCodeExecution("""
            x = []
            x.append("hello")
            x.append(5)
            print(x[0], x[1])
            """)

        # Existing list
        self.assertCodeExecution("""
            x = [1, 2, 3, 4]
            x.append(5)
            x.append("hello")
            print(x[4], x[5])
            """)

    def test_remove(self):
        # Remove integer
        self.assertCodeExecution("""
            x = [1, 2, 3]
            x.remove(1)
            print(x)
            """)

        # Remove only first duplicate
        self.assertCodeExecution("""
            x = [1, 2, 2, 3, 2]
            x.remove(2)
            print(x)
            """)

        # Remove boolean
        self.assertCodeExecution("""
            x = [True, False, True, False]
            x.remove(1)
            print(x)
            """)

        # Not in list
        self.assertCodeExecution("""
            x = [1, 2]
            x.remove(3)
            """)

    def test_slice(self):
        # Full slice
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print(x[:])
            """)

        # Left bound slice
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print(x[1:])
            """)

        # Right bound slice
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print(x[:4])
            """)

        # Slice bound in both directions
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print(x[1:4])
            """)

    def test_count(self):
        # Normal Count
        self.assertCodeExecution("""
            x = [1, 1, 1, 4, 5]
            print(x.count(1))
            """)

        # Bool Count
        self.assertCodeExecution("""
            x = [1, 1, False, 1, 4, True, 5, True]
            print(x.count(1))
            """)

        # Element doesn't exist count
        self.assertCodeExecution("""
            x = [1, False, 1, 1, True, 4, 5, True]
            print(x.count(2))
            """)

        self.assertCodeExecution("""
            x = [1, 1, 1, 4, 5, True]
            print(x.count(1))
            """)

    def test_contains(self):
        # Normal Contains
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print(x.contains(1))
            """)

        # Element doesn't exist
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print(x.contains(0))
            """)

        # Checking for boolean
        self.assertCodeExecution("""
            x = [True, False]
            print(x.count(1))
            """)

    def test_sort(self):
        self.assertCodeExecution("""
            fixtures = [
                [9, 4, 7],
                ['beta', 'theta', 'alpha'],
            ]
            for x in fixtures:
                x.sort()
                print(x)
            """)

        self.assertCodeExecution("""
            fixtures = [
                [9, 4, 7],
                ['beta', 'theta', 'alpha'],
            ]
            for x in fixtures:
                x.sort(reverse=True)
                print(x)
            """)

        self.assertCodeExecution("""
            def second(s):
                return s[1]

            x = ['abc', 'bza', 'cda', 'daa']
            x.sort(key=second)
            print(x)
            """)

        self.assertCodeExecution("""
            def second(s):
                return s[1]

            x = ['abc', 'bza', 'cda', 'daa']
            x.sort(key=second, reverse=True)
            print(x)
            """)

    def test_pop(self):
        self.assertCodeExecution("""
            x = [1, 2, 3]
            print(x.pop())
            print(x)
            """)

        self.assertCodeExecution("""
            x = [1, 2, 3]
            print(x.pop(0))
            print(x)
            """)

        self.assertCodeExecution("""
            x = [1, 2, 3]
            print(x.pop(-2))
            print(x)
            """)

    def test_pop_exceptions(self):
        self.assertCodeExecution("""
            x = []
            print(x.pop())
            print(x)
            """)

        self.assertCodeExecution("""
            x = [1, 2, 3]
            print(x.pop(3))
            print(x)
            """)

        self.assertCodeExecution("""
            x = [1, 2, 3]
            print(x.pop(-4))
            print(x)
            """)


class UnaryListOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'list'


class BinaryListOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'list'

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
        'test_ge_list',

        'test_gt_class',
        'test_gt_frozenset',
        'test_gt_list',

        'test_le_class',
        'test_le_frozenset',
        'test_le_list',

        'test_lshift_class',
        'test_lshift_frozenset',

        'test_lt_class',
        'test_lt_frozenset',
        'test_lt_list',

        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_frozenset',

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


class InplaceListOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'list'

    not_implemented = [
        'test_add_bytearray',
        'test_add_bytes',
        'test_add_class',
        'test_add_dict',
        'test_add_frozenset',
        'test_add_range',
        'test_add_set',
        'test_add_str',

        'test_and_class',
        'test_and_frozenset',

        'test_floor_divide_class',
        'test_floor_divide_complex',
        'test_floor_divide_frozenset',

        'test_lshift_class',
        'test_lshift_frozenset',

        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_frozenset',

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
