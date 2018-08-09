from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase

from unittest import expectedFailure


class DictTests(TranspileTestCase):
    def test_setattr(self):
        self.assertCodeExecution("""
            x = {}
            try:
                x.attr = 42
            except AttributeError as err:
                print(err)
            """)

    def test_getattr(self):
        self.assertCodeExecution("""
            x = {}
            try:
                print(x.attr)
            except AttributeError as err:
                print(err)
            """)

    def test_creation(self):
        # Empty dict
        self.assertCodeExecution("""
            x = {}
            print(x)
            """)

        self.assertCodeExecution("""
            x = {'a': 1}
            print(x)
            """)

    def test_getitem(self):
        # Simple existent key
        self.assertCodeExecution("""
            y = 37
            x = {'a': 1, 'b': 2, 'c': y}
            print('a' in x)
            print('a' not in x)
            print(x['a'])
            """)

        # Simple non-existent key
        self.assertCodeExecution("""
            x = {'a': 1, 'b': 2}
            print('c' in x)
            print('c' not in x)
            try:
                print(x['c'])
            except KeyError as err:
                print(err)
            """)

    def test_clear(self):
        # Clear a dictionary
        self.assertCodeExecution("""
            x = {'a': 1, 'b': 2}
            print('a' in x)
            print(x.clear())
            print('a' not in x)
            print(x)
            """)

        # Clear an already empty dict
        self.assertCodeExecution("""
            x = {}
            print('a' not in x)
            print(x.clear())
            print('a' not in x)
            print(x)
            """)

    def test_builtin_constructor(self):
        # Construct a dictionary using the dict builtin
        self.assertCodeExecution("""
            x = dict()
            print(x)
            print('a' in x)

            # List of tuples
            x = dict([('a', 1), ('b', 2)])
            print('a' in x)
            print(x['a'])
            print('c' in x)

            # List of lists
            x = dict([['a', 3], ['b', 4]])
            print('a' in x)
            print(x['a'])
            print('c' in x)

            # Tuple of lists
            x = dict((['a', 5], ['b', 6]))
            print('a' in x)
            print(x['a'])
            print('c' in x)

            # Tuple of tuples
            x = dict((('a', 5), ('b', 6)))
            print('a' in x)
            print(x['a'])
            print('c' in x)

            # Test __contains__ throws unhashable exception
            try:
                print([] in x)
            except TypeError as err:
                print(err)
            try:
                print([] not in x)
            except TypeError as err:
                print(err)
        """)

    def test_builtin_constructor_kwargs(self):
        self.assertCodeExecution("""
            d = dict(a=1, b=2)
            print('a' in d)
            print('b' in d)
            print('c' not in d)
            print(d['b'])

            d = dict(d, b=3)
            print('a' in d)
            print('b' in d)
            print('c' in d)
            print(d['b'])
        """)

    def test_builtin_non_2_tuples(self):
        # One of the elements isn't a 2-tuple
        self.assertCodeExecution("""
            try:
                x = dict([('a', 1), ('b', 2, False)])
            except ValueError as err:
                print(err)
            """)

    def test_builtin_non_sequence(self):
        # One of the elements isn't a sequence
        self.assertCodeExecution("""
            try:
                x = dict([('a', 1), False, ('b', 2)])
            except TypeError as err:
                print(err)
            """)

    def test_method_pop(self):
        self.assertCodeExecution("""
            x = {1: 2, 3: 4, 5: 6}
            print(x.pop(1))
            print(x.pop(3, 37))
            try:
                print(x.pop(7))
            except KeyError as e:
                print("Dict doesn't contain 7")
            print(x.pop(7, 42))
            print("Done")
            """)

    def test_method_popitem(self):
        self.assertCodeExecution("""
            ITEMS = [(1, 2), (3, ("4", 5))]
            x = dict(ITEMS)

            popped_1 = x.popitem()
            print(popped_1 in ITEMS)

            popped_2 = x.popitem()
            print(popped_2 in ITEMS and popped_2 != popped_1)

            # Check for exception
            try:
                print(x.popitem())
            except KeyError as err:
                print(err)
            """)

    def test_method_setdefault(self):
        self.assertCodeExecution("""
            x = {42: 'Babel'}
            print(x.setdefault(42)) # should return Babel

            print(x.setdefault(1)) # should return None
            print(x[1] == None) # should be True

            print(x.setdefault('David', 'Gilmour')) # should return 'Gilmour'

            # Check unhashable exceptions
            try:
                x.setdefault([], 42)
            except TypeError as err:
                print(err)
            """)

    def test_method_get(self):
        self.assertCodeExecution("""
            x = {1: 2}
            print(x.get(1))
            print(x.get(2))
            print(x.get(3,4))

            class MyClass:
                pass

            obj = MyClass()
            print(x.get(obj))
            """)

        # check for unhashable type errors
        self.assertCodeExecution("""
            x = {1: 2}

            try:
                print(x.get([]))
            except TypeError as err:
                print(err)

            try:
                print(x.get([], 1))
            except TypeError as err:
                print(err)

            try:
                print(x.get(list([1])))
            except TypeError as err:
                print(err)

            try:
                print(x.get(set([1, 2, 3])))
            except TypeError as err:
                print(err)

            try:
                print(x.get(iter([1, 2, 3])))
            except TypeError as err:
                print(err)

            try:
                print(x.get(slice(3)))
            except TypeError as err:
                print(err)
            """)

    def test_copy(self):
        self.assertCodeExecution("""
            x = {42: 'Babel'}
            y = x.copy()

            print(y)
            print(x == y)
            print(x is not y)
            """)

        self.assertCodeExecution("""
            x = {'42': 'Babel'}
            y = x.copy()

            print(x['42'] is y['42'])

            x['42'] = 'somevalue'
            print(x['42'] == y['42'])

            print(x == y)
            """)

    def test_fromkeys(self):
        self.assertCodeExecution("""
            keys = [1, 2]
            print(dict.fromkeys(keys))
            """)

        # non-iterable error test
        self.assertCodeExecution("""
            keys = 1
            value = 2
            try:
                print(dict.fromkeys(keys, value))
            except TypeError as err:
                print(err)
            """)

        # empty iterable and orginal dict test
        self.assertCodeExecution("""
            keys = ()
            value = 5
            dt = {}
            print(dt.fromkeys(keys, value))
            print(dt)
            """)

        # non-hashable error on key test
        self.assertCodeExecution("""
            keys = [[1], 2]
            try:
                print(dict.fromkeys(keys))
            except TypeError as err:
                print(err)
            """)

    def test_update(self):
        self.assertCodeExecution("""
            a = {}
            a.update([('a', 1), ('b', 2)])
            print(sorted(a))
            b = {}
            b.update({'a': 1, 'b':2})
            print(sorted(b))
            c = {}
            c.update(a=1, b=2)
            print(sorted(c))
        """)

        self.assertCodeExecution("""
            try:
                a = {}
                a.update([('a', 1, 2), ('b',2)])
                print('An error should have been raised!')
            except ValueError:
                print('Received a ValueError as expected')
        """)

        self.assertCodeExecution("""
            try:
                a = {}
                a.update('1')
                print('An error should have been raised')
            except ValueError:
                print('Received a ValueError as expected')
        """)

        self.assertCodeExecution("""
            try:
                a = {}
                a.update(1)
                print('An error should have been raised')
            except TypeError:
                print('Received a TypeError as expected')
        """)

        self.assertCodeExecution("""
            try:
                a = {}
                x = set([1, 2])
                a.update(x)
                print('An error should have been raised')
            except TypeError:
                print('Received a TypeError as expected')
        """)

    @expectedFailure
    def test_fromkeys_missing_iterable(self):
        self.assertCodeExecution("""
            try:
                print(dict.fromkeys())
            except TypeError as err:
                print(err)
            """)

    def test_values(self):
        self.assertCodeExecution("""
            x = {1 : 1,2 : 2,3 : 3}
            y = x.values()
            print(type(y))
            print(len(y))
            print(3 in y)
            print(42 not in y)
            if y:
                print('Working as expected')
            s = 0
            for i in y:
                s += i
            print(s)
            """)

        self.assertCodeExecution("""
            try:
                x = {1 : 1,2 : 2}
                print(x.values() * 'a')
                print('A TypeError should have been raised')
            except TypeError as err:
                print(err)
            """)

        self.assertCodeExecution("""
            try:
                x = {1 : 1,2 : 2,3 : 3}
                y = x.values()
                print(y[0])
                print('A TypeError should have been raised')
            except TypeError as err:
                print(err)
            """)

        self.assertCodeExecution("""
            try:
                x = {1 : 1,2 : 2,3 : 3}
                y = x.values()
                print(y['a'])
                print('A TypeError should have been raised')
            except TypeError as err:
                print(err)
            """)

        self.assertCodeExecution("""
            try:
                x = {1 : 1,2 : 2,3 : 3}
                y = x.values()
                y[0] = 7
                print('A TypeError should have been raised')
            except TypeError as err:
                print(err)
            """)

        self.assertCodeExecution("""
            try:
                x = {1 : 1,2 : 2,3 : 3}
                y = x.values()
                del y[0]
                print('A TypeError should have been raised')
            except TypeError as err:
                print(err)
            """)

        self.assertCodeExecution("""
            try:
                x = {1 : 1,2 : 2,3 : 3}
                y = x.values()
                print(+y)
                print('A TypeError should have been raised')
            except TypeError as err:
                print(err)
            """)

        self.assertCodeExecution("""
            try:
                x = {1 : 1,2 : 2,3 : 3}
                y = x.values()
                print(-y)
                print('A TypeError should have been raised')
            except TypeError as err:
                print(err)
            """)

        self.assertCodeExecution("""
            try:
                x = {1 : 1,2 : 2,3 : 3}
                y = x.values()
                print(~y)
                print('A TypeError should have been raised')
            except TypeError as err:
                print(err)
            """)

    def test_items(self):
        self.assertCodeExecution("""
            x = {1 : 1,2 : 2,3 : 3}
            x2 = {1 : 1,2 : 2,3 : 3,4 : 4}
            y = x.items()
            y2 = x2.items()
            print(len(y))
            print((1,1) in y)
            print((1,2) not in y)
            s1 = 0
            s2 = 0
            for i,j in y:
                s1 += i
                s2 += j
            print(s1)
            print(s2)
            s = {(1,1),(1,2),(2,2),(2,3)}
            print(len(y & s))
            print(len(y | s))
            print(len(y ^ s))
            print(len(y - s))
            """)


class UnaryDictOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'dict'


class BinaryDictOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'dict'

    not_implemented = [
        'test_multiply_bytearray',

        'test_subscr_bytearray',
        'test_subscr_class',
        'test_subscr_complex',

    ]


class InplaceDictOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'dict'
