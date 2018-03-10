from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class FrozensetTests(TranspileTestCase):
    def test_creation(self):
        # Empty dict
        self.assertCodeExecution("""
            x = frozenset()
            print(x)

            x = frozenset({'a'})
            print(x)

            y = {1,2}
            x = frozenset(y)
            print(x)
            y = {3}
            print(x)

            y = ['c']
            x = frozenset(y)
            print(x)
            y.append('d')
            print(x)

            y = (1,2)
            x = frozenset(y)
            print(x)
            y = ()
            print(x)

            y ='a'
            x = frozenset(y)
            print(x)
            y = y + 'b'
            print(x)

            """)

    def test_contains(self):
        # Normal Contains
        self.assertCodeExecution("""
            x = frozenset()
            print(1 in x)

            x = frozenset({'a'})
            print('a' in x)
            print('b' in x)

            y = {1,2}
            x = frozenset(y)
            print(2 in x)
            print(3 in x)

            y = ['c']
            x = frozenset(y)
            print('c' in x)
            print('a' in x)

            y = (1,2)
            x = frozenset(y)
            print(3 in x)
            print(1 in x)

            y = 'a'
            x = frozenset(y)
            print('e' in x)
            print('a' in x)

            """)

    def test_not_contains(self):
        # Normal Not Contains
        self.assertCodeExecution("""
            x = frozenset()
            print(1 in x)

            x = frozenset({'a'})
            print('b' not in x)
            print('a' not in x)

            y = {1,2}
            x = frozenset(y)
            print(4 not in x)
            print(1 not in x)

            y = ['c']
            x = frozenset(y)
            print('d' not in x)
            print('c' not in x)

            y = (1,2)
            x = frozenset(y)
            print(1 not in x)
            print(3 not in x)

            y = 'a'
            x = frozenset(y)
            print('a' not in x)
            print('d' not in x)

            """)

    def test_iteration(self):
        self.assertCodeExecution("""
            x = {1, 2, 3}
            y = frozenset()
            #We are not printing each element because python and voc store the items in different ways.
            for s in x:
                print(x.__contains__(s))
            for s in y:
                print(y.__conatins__(s))

            """)

    def test_copy(self):
        self.assertCodeExecution("""
            x = frozenset()
            y = x.copy()
            print(x is y)

            x = frozenset({'a'})
            y = x.copy()
            print(x is y)

            y = {1,2}
            x = frozenset(y)
            z = x.copy()
            print(x is z)

            y = ['c']
            x = frozenset(y)
            z = x.copy()
            print(x is z)

            y = (1,2)
            x = frozenset(y)
            z = x.copy()
            print(x is z)

            y = 'a'
            x = frozenset(y)
            z = x.copy()
            print(x is z)

            """)

    def test_isdisjoint(self):
        self.assertCodeExecution("""
            x = frozenset("hello world")
            y = set("hello")
            z = frozenset()
            t = "hello"
            w = 2.0

            print(x.isdisjoint(y))
            print(x.isdisjoint(z))

            # iterable test
            print(x.isdisjoint(t))

            # not-iterable test
            try:
                print(x.isdisjoint(w))
            except TypeError as err:
                print(err)
            """)

    def test_issubset(self):
        self.assertCodeExecution("""
            a = frozenset('abc')
            b = frozenset('abcde')
            c = set()
            d = 'wxyz'

            print(a.issubset(b))
            print(a.issubset(a))
            print(a.issubset(c))

            # iterable test
            print(a.issubset(d))
            """)

        # not-iterable test
        self.assertCodeExecution("""
            a = frozenset({1, 2, 3})
            b = 1
            try:
                print(a.issubset(b))
            except TypeError as err:
                print(err)
            """)

    def test_issuperset(self):
        self.assertCodeExecution("""
            a = frozenset('abcd')
            b = frozenset('ab')
            c = set()
            d = 'ab'

            print(a.issuperset(b))
            print(a.issuperset(a))
            print(a.issuperset(c))

            # iterable test
            print(a.issuperset(d))
            """)

        # not-iterable test
        self.assertCodeExecution("""
            a = frozenset({1, 2, 3})
            b = 1
            try:
                print(a.issuperset(b))
            except TypeError as err:
                print(err)
            """)

    def test_union(self):
        self.assertCodeExecution("""
            x = frozenset({1, 2, 3})
            y = frozenset({3, 4, 5})
            z = [5, 6, 7]
            w = 1
            t = frozenset()

            print(x.union(y))

            # empty set test
            print(x.union(t))

            # multiple args test
            print(x.union(y, z))

            # iterable test
            print(x.union(z))

            # not-iterable test
            try:
                print(x.union(w))
            except TypeError as err:
                print(err)
            """)

    def test_intersection(self):
        self.assertCodeExecution("""
            x = frozenset({1, 2, 3})
            y = frozenset({2, 3, 4})
            z = [3, 6, 7]
            w = 1
            t = frozenset()

            print(x.intersection(y))

            # empty set test
            print(x.intersection(t))

            # multiple args test
            print(x.intersection(y, z))

            # iterable test
            print(x.intersection(z))

            # not-iterable test
            try:
                print(x.intersection(w))
            except TypeError as err:
                print(err)
            """)

    def test_difference(self):
        self.assertCodeExecution("""
            x = frozenset({1, 2, 3})
            y = frozenset({2, 3, 4})
            z = [1, 6]
            w = 1
            t = frozenset()

            print(x.difference(y))

            # empty set test
            print(x.difference(t))

            # multiple args test
            print(x.difference(y, z))

            # iterable test
            print(x.difference(z))

            # not-iterable test
            try:
                print(x.difference(w))
            except TypeError as err:
                print(err)
            """)

    def test_symmetric_difference(self):
        self.assertCodeExecution("""
            x = frozenset({1, 2, 3})
            y = frozenset({2, 3, 4})
            z = [1, 6, 7]
            w = 1
            t = frozenset()

            print(x.symmetric_difference(y))

            # empty set test
            print(x.symmetric_difference(t))

            # iterable test
            print(x.symmetric_difference(z))

            # not-iterable test
            try:
                print(x.symmetric_difference(w))
            except TypeError as err:
                print(err)

            """)


class UnaryFrozensetOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'frozenset'


class BinaryFrozensetOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'frozenset'

    not_implemented = [
        'test_subscr_bool',
        'test_subscr_bytearray',
        'test_subscr_bytes',
        'test_subscr_class',
        'test_subscr_complex',
        'test_subscr_dict',
        'test_subscr_float',
        'test_subscr_frozenset',
        'test_subscr_int',
        'test_subscr_list',
        'test_subscr_None',
        'test_subscr_NotImplemented',
        'test_subscr_range',
        'test_subscr_set',
        'test_subscr_slice',
        'test_subscr_str',
        'test_subscr_tuple',
    ]


class InplaceFrozensetOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'frozenset'
