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
            w = x.difference([3,4,5])
            print(x)
            print(y)
            print(z)
            print(w)
            """)

        # not iterable test
        self.assertCodeExecution("""
            x = set([1, 2, 3])
            try:
                print(x.difference(1))
            except TypeError as err:
                print(err)
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

    def test_isdisjoint(self):
        # successful
        self.assertCodeExecution("""
            x = set("hello World !")
            y = set("hello")
            z = set()
            t = set()
            print(x.isdisjoint(y))
            print(x.isdisjoint("hell"))
            print(x.isdisjoint(z))
            print(t.isdisjoint(z))
            print(t.isdisjoint(y))
            """)

        # unsuccessful
        self.assertCodeExecution("""
            x = 9.3
            y = 5
            l = set("hello World !")
            m = set("hello")
            try:
                print(l.isdisjoint(y))
            except TypeError as err:
                print(err)
            try:
                print(l.isdisjoint(x))
            except TypeError as err:
                print(err)
            try:
                print(l.isdisjoint(x))
            except TypeError as err:
                print(err)
            """)

    def test_issubset(self):
        self.assertCodeExecution("""
            a = set('abc')
            b = set('abcde')
            c = set()
            print(a.issubset(b))
            print(a.issubset('ab'))
            print(a.issubset(a))
            print(a.issubset(c))
            """)

        # not iterable test
        self.assertCodeExecution("""
            a = {1, 2, 3}
            try:
                print(a.issubset(1))
            except TypeError as err:
                print(err)
            """)

    def test_issuperset(self):
        self.assertCodeExecution("""
            a = set('abcd')
            b = set('ab')
            c = set()
            print(a.issuperset(b))
            print(a.issuperset('ab1'))
            print(a.issuperset(a))
            print(a.issuperset(c))
            """)

        # not iterable test
        self.assertCodeExecution("""
            a = {1, 2, 3}
            try:
                print(a.issuperset(1))
            except TypeError as err:
                print(err)
            """)

    def test_symmetric_difference(self):
        # successful
        self.assertCodeExecution("""
            x = set("hello World !")
            y = set("hello")
            z = set()
            t = set()
            print(sorted(x.symmetric_difference(y)))
            print(sorted(x.symmetric_difference(z)))
            print(sorted(t.symmetric_difference(z)))
            print(sorted(t.symmetric_difference(y)))
            """)

        # unsuccessful
        self.assertCodeExecution("""
            x = 9.3
            y = 5
            l = set("hello World !")
            m = set("hello")
            try:
                print(l.symmetric_difference(y))
            except TypeError as err:
                print(err)
            try:
                print(l.symmetric_difference(x))
            except TypeError as err:
                print(err)
            try:
                print(l.symmetric_difference())
            except TypeError as err:
                print(err)
            """)

    def test_symmetric_difference_update(self):
        # successful
        self.assertCodeExecution("""
            x = set("hello World !")
            y = set("hello")
            z = set()
            t = set()
            x.symmetric_difference_update(y)
            print(sorted(x))
            #x.test_symmetric_difference_update(z)
            print(sorted(x))
            t.symmetric_difference_update(z)
            print(sorted(t))
            t.symmetric_difference_update(y)
            print(sorted(t))
            """)

        # unsuccessful
        self.assertCodeExecution("""
            x = 9.3
            y = 5
            l = set("hello World !")
            m = set("hello")
            try:
                print(l.symmetric_difference_update(y))
            except TypeError as err:
                print(err)
            try:
                print(l.symmetric_difference_update(x))
            except TypeError as err:
                print(err)
            try:
                print(l.symmetric_difference_update())
            except TypeError as err:
                print(err)
            """)


class UnarySetOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'set'


class BinarySetOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'set'


class InplaceSetOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'set'
