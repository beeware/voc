from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class ListTests(TranspileTestCase):
    def test_setattr(self):
        self.assertCodeExecution("""
            x = [1, 2, 3]
            try:
                x.attr = 42
            except AttributeError as err:
                print(err)
            """)

    def test_getattr(self):
        self.assertCodeExecution("""
            x = [1, 2, 3]
            try:
                print(x.attr)
            except AttributeError as err:
                print(err)
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
            try:
                print(x[10])
            except IndexError as err:
                print(err)
            """)

        # Negative index out of range
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            try:
                print(x[-10])
            except IndexError as err:
                print(err)
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
            try:
                x[0] = 5
            except AttributeError as err:
                print(err)
            """)

        # Out of bounds (negative)
        self.assertCodeExecution("""
            x = [1]
            try:
                x[-2] = 5
            except AttributeError as err:
                print(err)
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
            try:
                x.remove(3)
            except ValueError as err:
                print(err)
            print(x)
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

        # Slice bound in both directions with end out of bounds
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print(x[1:6])
            """)

        # Slice bound in both directions with start out of bounds
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print(x[6:7])
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
            print(1 in x)
            """)

        # Element doesn't exist
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print(0 in x)
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
            try:
                print(x.pop())
            except IndexError as err:
                print(err)
            print(x)
            """)

        self.assertCodeExecution("""
            x = [1, 2, 3]
            try:
                print(x.pop(3))
            except IndexError as err:
                print(err)
            print(x)
            """)

        self.assertCodeExecution("""
            x = [1, 2, 3]
            try:
                print(x.pop(-4))
            except IndexError as err:
                print(err)
            print(x)
            """)

    def test_copy(self):
        self.assertCodeExecution("""
            x = [1, 2, 3]
            y = x.copy()
            print(y)
            """)

        self.assertCodeExecution("""
            x = [1, 2, 3]
            y = x.copy()
            print(x == y)
            """)

        self.assertCodeExecution("""
            x = [1, 2, 3]
            y = x.copy()
            print(x is not y)
            """)

        self.assertCodeExecution("""
            x = [1, 2, 3]
            y = x.copy()
            y.append(4)
            print(x == y)
            """)

        self.assertCodeExecution("""
            x = [[1], 2, 3]
            y = x.copy()
            print(x[0] is y[0])
            """)

    def test_index(self):
        self.assertCodeExecution("""
            x = [1, 2, 3]
            print(x.index(1))
            """)

        self.assertCodeExecution("""
            x = [1, 2, 1]
            print(x.index(1, 1))
            """)

        self.assertCodeExecution("""
            x = [1, 2, 3, 4]
            print(x.index(4, 0, len(x)))
            """)

        self.assertCodeExecution("""
            x = [1, 2, 3, 4]
            print(x.index(2, 1, 2))
            """)

        self.assertCodeExecution("""
            x = [1, 2, 3, 4]
            print(x.index(2, 0, 10))
            """)

        self.assertCodeExecution("""
            x = [1, 2, 1]
            print(x.index(1, 0, -2))
            """)

        self.assertCodeExecution("""
            x = [1, 2, 1]
            print(x.index(1, -3, -2))
            """)

        # cases for 'ValueError: not in list'
        self.assertCodeExecution("""
            x = [1, 2, 3]
            try:
                print(x.index(4))
            except ValueError as err:
                print(err)

            x = [1, 2, 1]
            try:
                print(x.index(2, 0, 1))
            except ValueError as err:
                print(err)

            x = [1, 2, 3, 4]
            try:
                print(x.index(4, 0, 3))
            except ValueError as err:
                print(err)

            x = [1, 2, 1]
            try:
                print(x.index(3, 0, 10))
            except ValueError as err:
                print(err)

            x = [1, 2, 3, 4]
            try:
                print(x.index(2, 10, 20))
            except ValueError as err:
                print(err)

            x = [1, 2, 3, 4]
            try:
                print(x.index(2, 10, 0))
            except ValueError as err:
                print(err)

            x = []
            try:
                print(x.index(1, 0, 10))
            except ValueError as err:
                print(err)
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
