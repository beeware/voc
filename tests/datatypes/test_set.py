from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class SetTests(TranspileTestCase):
    def test_setattr(self):
        self.assertCodeExecution("""
            x = {1, 2, 3}
            try:
                x.attr = 42
            except AttributeError as err:
                print(err)
            """)

    def test_getattr(self):
        self.assertCodeExecution("""
            x = {1, 2, 3}
            try:
                print(x.attr)
            except AttributeError as err:
                print(err)
            """)

    def test_creation(self):
        # Empty dict
        self.assertCodeExecution("""
            x = set()
            print(x)
            """)

        # Set constant
        self.assertCodeExecution("""
            x = {'a'}
            print(x)
            """)

        self.assertCodeExecution("""
            x = set(['a'])
            print(x)
            """)

    def test_getitem(self):
        # Simple existent key
        self.assertCodeExecution("""
            x = {'a', 'b'}
            print('a' in x)
            """)

        # Simple non-existent key
        self.assertCodeExecution("""
            x = {'a', 'b'}
            print('c' in x)
            """)

    def test_pop(self):
        # Test empty set popping.
        self.assertCodeExecution("""
            x = set()
            try:
                x.pop()
            except KeyError as err:
                print(err)
        """)

        # Test populated set popping.
        self.assertCodeExecution("""
            x = {'a'}
            print(len(x) == 1)
            x.pop()
            print(len(x) == set())
        """)

        # Test popping returns from set.
        self.assertCodeExecution("""
            x = {'a', 'b', 'c', 'd', 'e'}
            y = x.pop()
            print(y in x)
        """)

    def test_copy(self):
        self.assertCodeExecution("""
            x = {1, 2, 3}
            y = x.copy()
            print(x == y)
            print(x is not y)
            """)

        # ensures that it did a shallow copy
        self.assertCodeExecution("""
            x = {(1, 2, 3)}
            y = x.copy()
            print(x.pop() is y.pop())
            """)

    def test_difference(self):
        self.assertCodeExecution("""
            x = {1, 2, 3}
            y = {3, 4, 5}
            z = x.difference(y)
            print(x)
            print(y)
            print(z)
            """)

    def test_discard(self):
        self.assertCodeExecution("""
            x = {1, 2, 3}
            x.discard(1)
            x.discard(4)
            print(x)
            """)

    def test_intersection(self):
        self.assertCodeExecution("""
            x = {1, 2, 3}
            y = {3, 4, 5}
            z = x.intersection(y)
            w = x.intersection([3,4,5])
            print(x)
            print(y)
            print(z)
            print(w)
            """)

        self.assertCodeExecution("""
            x = {1, 2, 3}
            y = {4, 5}
            z = x.intersection(y)
            print(x)
            print(y)
            print(z)
            """)

        # not iterable test
        self.assertCodeExecution("""
            x = set([1, 2, 3])
            try:
                print(x.intersection(1))
            except TypeError as err:
                print(err)
            """)

    def test_remove(self):
        self.assertCodeExecution("""
            x = {1, 2, 3}
            x.remove(1)
            try:
                x.remove(4)
            except KeyError as err:
                print(err)
            print(x)
            """)

    def test_union(self):
        self.assertCodeExecution("""
            x = {1, 2, 3}
            y = {3, 4, 5}
            z = x.union(y)
            print(x)
            print(y)
            print(z)
            """)

    def test_difference_update(self):
        self.assertCodeExecution("""
            x = {1, 2, 3}
            y = {3, 4, 5}
            x.difference_update(y)
            print(x)
            """)

    def test_intersection_update(self):
        self.assertCodeExecution("""
            x = {1, 2, 3}
            y = {3, 4, 5}
            x.intersection_update(y)
            print(x)
            """)

    def test_update(self):
        self.assertCodeExecution("""
            x = {1, 2, 3}
            y = {3, 4, 5}
            print(x.update(y))
            print(x)
            """)

    def test_iteration(self):
        self.assertCodeExecution("""
            x = {1, 2, 3}
            y = set()
            #We are not printing each element because python and voc store the items in different ways.
            for s in x:
                print(x.__contains__(s))
            for s in y:
                print(y.__conatins__(s))
            """)

    def test_issubset(self):
        self.assertCodeExecution("""
            a = set('abc')
            b = set('abcde')
            print(a.issubset(b))
            print(a.issubset('ab'))
            """)

        # not iterable test
        self.assertCodeExecution("""
            a = set([1, 2, 3])
            try:
                print(a.issubset(1))
            except TypeError as err:
                print(err)
            """)

    def test_issuperset(self):
        self.assertCodeExecution("""
            a = set('abcd')
            b = set('ab')
            print(a.issuperset(b))
            print(a.issuperset('ab1'))
            """)

        # not iterable test
        self.assertCodeExecution("""
            a = set([1, 2, 3])
            try:
                print(a.issuperset(1))
            except TypeError as err:
                print(err)
            """)


class UnarySetOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'set'


class BinarySetOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'set'

    not_implemented = [
        'test_add_class',
        'test_add_frozenset',

        'test_and_class',

        'test_direct_eq_bytes',
        'test_direct_eq_set',
        'test_direct_ge_bytearray',
        'test_direct_ge_bytes',
        'test_direct_ge_set',
        'test_direct_gt_bytearray',
        'test_direct_gt_bytes',
        'test_direct_gt_set',
        'test_direct_le_bytearray',
        'test_direct_le_bytes',
        'test_direct_le_set',
        'test_direct_lt_bytearray',
        'test_direct_lt_bytes',
        'test_direct_lt_set',
        'test_direct_ne_bytearray',
        'test_direct_ne_bytes',
        'test_direct_ne_set',

        'test_direct_eq_frozenset',
        'test_direct_ge_frozenset',
        'test_direct_gt_frozenset',
        'test_direct_le_frozenset',
        'test_direct_lt_frozenset',
        'test_direct_ne_frozenset',

        'test_direct_eq_list',

        'test_direct_eq_slice',
        'test_direct_ne_slice',
        'test_direct_ge_slice',
        'test_direct_le_slice',

        'test_direct_gt_tuple',
        'test_direct_le_tuple',

        'test_eq_class',
        'test_eq_frozenset',

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

        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_frozenset',

        'test_multiply_bytearray',
        'test_multiply_bytes',
        'test_multiply_class',
        'test_multiply_frozenset',

        'test_ne_class',
        'test_ne_frozenset',

        'test_or_class',

        'test_power_class',
        'test_power_frozenset',

        'test_rshift_class',
        'test_rshift_frozenset',

        'test_subtract_class',

        'test_subscr_class',
        'test_subscr_frozenset',

        'test_true_divide_class',
        'test_true_divide_frozenset',

        'test_xor_class',
        'test_xor_frozenset',
        'test_xor_set',
    ]


class InplaceSetOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'set'

    not_implemented = [
        'test_add_class',
        'test_add_frozenset',

        'test_and_class',
        'test_and_frozenset',
        'test_and_set',

        'test_lshift_class',
        'test_lshift_frozenset',

        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_frozenset',

        'test_multiply_class',
        'test_multiply_frozenset',

        'test_or_class',
        'test_or_frozenset',
        'test_or_set',

        'test_power_class',
        'test_power_frozenset',

        'test_rshift_class',
        'test_rshift_frozenset',

        'test_subtract_class',
        'test_subtract_frozenset',
        'test_subtract_set',

        'test_true_divide_class',
        'test_true_divide_frozenset',

        'test_xor_class',
        'test_xor_frozenset',
        'test_xor_set',
    ]
