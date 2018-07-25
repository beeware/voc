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
