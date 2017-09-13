from itertools import permutations
from .. utils import (
    BinaryOperationTestCase,
    InplaceOperationTestCase,
    SAMPLE_SUBSTITUTIONS,
    TranspileTestCase,
    UnaryOperationTestCase,
)


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
            except IndexError as err:
                print(err)
            """)

        # Out of bounds (negative)
        self.assertCodeExecution("""
            x = [1]
            try:
                x[-2] = 5
            except IndexError as err:
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

    def extend_substitutions(self, prefix, suffix):
        possible_vals = []
        for perm in permutations(suffix):
            possible_vals.append(repr(prefix + list(perm)))
        return possible_vals

    def test_extend(self):
        # extend a list
        self.assertCodeExecution("""
            x = [1, 2, 3]
            x.extend([4, "hello"])
            print(x)
            """)

        # extend a tuple
        x = [1, 2, 3]
        y = [5, "world", "hello"]
        self.assertCodeExecution("""
            x = %(x)s
            x.extend(%(y)s)
            print(x)
            """ % {
                'x': x,
                'y': y,
            },
            substitutions={repr(x + y): self.extend_substitutions(x, y)})

        # extend a frozenset
        x = [1, 2, 3]
        y = [8, "theta"]
        self.assertCodeExecution("""
            x = %(x)s
            y = frozenset(%(y)s)
            x.extend(y)
            """ % {
                'x': x,
                'y': y,
            },
            substitutions={repr(x + y): self.extend_substitutions(x, y)})

        # extend a set
        x = [1, 2, 3]
        y = ["beta", "alpha"]
        self.assertCodeExecution("""
            x = %(x)s
            y = set(%(y)s)
            x.extend(y)
            """ % {
                'x': x,
                'y': y,
            },
            substitutions={repr(x + y): self.extend_substitutions(x, y)})

        # extend a dict
        x = [1, 2, 3]
        y = {"alpha": 4, "theta": 6, "beta": 5}
        keys = list(y.keys())
        self.assertCodeExecution("""
            x = %(x)s
            y = %(y)s
            x.extend(y)
            """ % {
                'x': x,
                'y': y,
            },
            substitutions={repr(x + keys): self.extend_substitutions(x, keys)})

        # extend an iterator
        self.assertCodeExecution("""
            x = [1, 2, 3]
            x.extend(iter([4,5,6]))
            print(x)
            """)

        # extend bytearray
        self.assertCodeExecution("""
            x = [1, 2, 3]
            x.extend(bytearray(b'abc'))
            print(x)
            """)

        # extend byte
        self.assertCodeExecution("""
            x = [1, 2, 3]
            x.extend(b'def')
            print(x)
            """)

        # extend str
        self.assertCodeExecution("""
            x = [1, 2, 3]
            x.extend(b'string')
            print(x)
            """)

        # extend range
        self.assertCodeExecution("""
            x = [1, 2, 3]
            x.extend(range(5))
            print(x)
            """)

        # extend non-iterable
        self.assertCodeExecution("""
            x = [1, 2, 3]
            try:
                x.extend(4)
            except TypeError as err:
                print(err)
            print(x)
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

    def test_reverse(self):
        # New list
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            x.reverse()
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

    # when step is 0
    def test_slice_with_zero_step(self):
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            try:
                print(x[1:3:0])
            except ValueError as err:
                print(err)
            """)

    def test_slice_in_reverse(self):
        # Full slice with a negative step
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print (x[::-1])
            """)

        # left bound slice with a negative step
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print (x[4::-2])
            """)

        # Right bound slice with a negative step
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print (x[:4:-1])
            """)

        # Right bound and left bound slice with a negative step
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print (x[1:4:-2])
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

    def test_insert(self):
        self.assertCodeExecution("""
            x = [1, 2, 3]
            x.insert(0, 4)
            print(x)
            x.insert(1, 5)
            print(x)
            x.insert(len(x), 6)
            print(x)
            x.insert(200, 7)
            print(x)
            x.insert(-1, 8)
            print(x)
            x.insert(-len(x), 9)
            print(x)
            x.insert(-200, 10)
            print(x)
            """)

        self.assertCodeExecution("""
            x = [1, 2, 3]
            x.insert(0, "hello")
            print(x)
            """)

        self.assertCodeExecution("""
            x = [1, 2, 3]
            x.insert(0, [1, 2])
            print(x)
            """)

        # cases for 'TypeError: wrong type'
        self.assertCodeExecution("""
            x = [1, 2, 3]
            try:
                print(x.insert('a', 4))
            except TypeError as err:
                print(err)

            x = [1, 2, 3]
            try:
                print(x.insert([1,2,3], 4))
            except TypeError as err:
                print(err)
            """)

    def test_lt_reflected(self):
        self.assertCodeExecution("""
            class A:
                def __gt__(self, other):
                    return True

            x = A()
            y = A()

            # verify that A doesn't have __lt__()
            print(x.__lt__(x))

            # ensure rich comparison logic is used
            print([x] < [x]) # False, x is x and same size
            print([x] < [y]) # True, x is not y, reflected

            # when elements are non-identical, return that comparison, even if size is not
            print([x, y] < [y]) # True, x is not y, reflected

            # ensure tie breaker by size is still used when identical elements
            print([x, y] < [x]) # False, larger size
            print([x] < [x, y]) # True, smaller size
            """)

    def test_le_reflected(self):
        self.assertCodeExecution("""
            class A:
                def __ge__(self, other):
                    return True

            x = A()
            y = A()

            # verify that A doesn't have __le__()
            print(x.__le__(x))

            # ensure rich comparison logic is used
            print([x] <= [x]) # False, x is x and same size
            print([x] <= [y]) # True, x is not y, reflected

            # when elements are non-identical, return that comparison, even if size is not
            print([x, y] <= [y]) # True, x is not y, reflected

            # ensure tie breaker by size is still used when identical elements
            print([x, y] <= [x]) # False, larger size
            print([x] <= [x, y]) # True, smaller size
            """)

    def test_gt_reflected(self):
        self.assertCodeExecution("""
            class A:
                def __lt__(self, other):
                    return True

            x = A()
            y = A()

            # verify that A doesn't have __gt__()
            print(x.__gt__(x))

            # ensure rich comparison logic is used
            print([x] > [x]) # False, x is x and same size
            print([x] > [y]) # True, x is not y, reflected

            # when elements are non-identical, return that comparison, even if size is not
            print([x, y] > [y]) # True, x is not y, reflected

            # ensure tie breaker by size is still used when identical elements
            print([x, y] > [x]) # False, larger size
            print([x] > [x, y]) # True, smaller size
            """)

    def test_ge_reflected(self):
        self.assertCodeExecution("""
            class A:
                def __le__(self, other):
                    return True

            x = A()
            y = A()

            # verify that A doesn't have __ge__()
            print(x.__ge__(x))

            # ensure rich comparison logic is used
            print([x] >= [x]) # False, x is x and same size
            print([x] >= [y]) # True, x is not y, reflected

            # when elements are non-identical, return that comparison, even if size is not
            print([x, y] >= [y]) # True, x is not y, reflected

            # ensure tie breaker by size is still used when identical elements
            print([x, y] >= [x]) # False, larger size
            print([x] >= [x, y]) # True, smaller size
            """)

    def test_eq_reflected(self):
        self.assertCodeExecution("""
            class A:
                def __eq__(self, other):
                    return True

            class B:
                def __eq__(self, other):
                    return False

            x = A()
            y = B()

            print([x] == [x]) # True, identity implies equality
            print([x, x] == [x]) # False, size not equal

            print([x] == [y]) # True, x is not y, x.__eq__(y)
            print([y] == [x]) # False, y is not x, y.__eq__(x)
            """)

    def test_reversed(self):
        self.assertCodeExecution("""
            list = [123, 'xyz', 'abc']
            reversedList = ['abc', 'xyz', 123] # to check equality
            l = []
            reverse = list.__reversed__()
            try:
                while(True):
                    l.append(next(reverse))
            except StopIteration:
                print(l == reversedList)

            origList = [123, 'xyz', 'abc'] # to check if original list was modified
            print(list == origList)
        """)


class UnaryListOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'list'


class BinaryListOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'list'

    not_implemented = [
        'test_subscr_bool',
    ]


class InplaceListOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'list'

    # Several tests add a list to an iterable with a non-deterministic
    # ordering. We define these substitutions here where the first part of the
    # values are the list (in its original order) and the last part is the
    # non-deterministic iterable.
    substitutions = {}
    for prefix in (
        [],
        ['a', 'b', 'c'],
        [3, 4, 5],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    ):
        for suffix in (
            [1, 2.3456, 7],
            ['on', 'to', 'an'],
            ['one', 'two', 'six'],
            ['a', 'd', 'c'],
        ):
            from_vals = []
            for perm in permutations(suffix):
                from_vals.append(repr(prefix + list(perm)))
            substitutions[repr(prefix + suffix)] = from_vals

    substitutions.update(SAMPLE_SUBSTITUTIONS)
