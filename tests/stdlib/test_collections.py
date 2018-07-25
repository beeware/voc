from unittest import expectedFailure

from ..utils import TranspileTestCase


class CollectionsModuleTests(TranspileTestCase):

    #######################################################
    # __doc__
    def test___doc__(self):
        self.assertCodeExecution("""
            import collections
            print(collections.__doc__)
            """)

    #######################################################
    # __file__
    @expectedFailure
    def test___file__(self):
        self.assertCodeExecution("""
            import collections
            print(collections.__file__)
            """)

    #######################################################
    # __loader__
    @expectedFailure
    def test___loader__(self):
        self.assertCodeExecution("""
            import collections
            print(collections.__loader__)
            """)

    #######################################################
    # __name__
    def test___name__(self):
        self.assertCodeExecution("""
            import collections
            print(collections.__name__)
            """)

    #######################################################
    # __package__
    def test___package__(self):
        self.assertCodeExecution("""
            import collections
            print(collections.__package__)
            """)

    #######################################################
    # __spec__
    @expectedFailure
    def test___spec__(self):
        self.assertCodeExecution("""
            import collections
            print(collections.__spec__)
            """)

    #######################################################
    # namedtuple
    @expectedFailure
    def test_namedtuple(self):
        self.assertCodeExecution("""
            import collections
            print(collections.namedtuple('Point', ['x', 'y']))
            """)

    #######################################################
    # ChainMap
    @expectedFailure
    def test_ChainMap(self):
        self.assertCodeExecution("""
            import collections
            print(collections.ChainMap())
            """)

    #######################################################
    # Counter
    @expectedFailure
    def test_Counter(self):
        self.assertCodeExecution("""
            import collections
            print(collections.Counter())
            """)

    #######################################################
    # UserDict
    @expectedFailure
    def test_UserDict(self):
        self.assertCodeExecution("""
            import collections
            print(collections.UserDict())
            """)

    #######################################################
    # UserList
    @expectedFailure
    def test_UserList(self):
        self.assertCodeExecution("""
            import collections
            print(collections.UserList())
            """)

    #######################################################
    # UserString
    @expectedFailure
    def test_UserString(self):
        self.assertCodeExecution("""
            import collections
            print(collections.UserString("Hello World"))
            """)


class DequeTests(TranspileTestCase):

    pass


class OrderedDictTests(TranspileTestCase):

    pass


class DefaultDictTests(TranspileTestCase):

    def test_creation(self):
        self.assertCodeExecution("""
            import collections
            print(collections.defaultdict())
            print(collections.defaultdict(int))
            print(collections.defaultdict(list, {'a': 1}))
            """)

    def test_superclass_method(self):
        self.assertCodeExecution("""
            import collections
            d = collections.defaultdict(int)
            print(d.get("key"))
            print(d.setdefault("default"))
            print(d)
            """)

    def test_default_list(self):
        self.assertCodeExecution("""
            from collections import defaultdict

            s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
            d = defaultdict(list)
            for k, v in s:
                d[k].append(v)
            print(sorted(d.items()))
            """)

    def test_default_int(self):
        self.assertCodeExecution("""
            from collections import defaultdict

            s = 'mississippi'
            d = defaultdict(int)
            for k in s:
                d[k] += 1
            print(sorted(d.items()))
            """)

    @expectedFailure
    def test_default_function_object(self):
        self.assertCodeExecution("""
            from collections import defaultdict

            def constant_factory(value):
                return lambda: value
            d = defaultdict(constant_factory('<missing>'))
            d.update(name='John', action='ran')
            print('%(name)s %(action)s to %(object)s' % d)
            """)

    def test_default_set(self):
        self.assertCodeExecution("""
            from collections import defaultdict

            s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
            d = defaultdict(set)
            for k, v in s:
                d[k].add(v)
            print(sorted(d.items()))
            """)
