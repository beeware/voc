from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class EnumerateTests(TranspileTestCase):
    def test_enumerate(self):
        self.assertCodeExecution("""
            lst=['a','b','c','d','e']
            print(list(enumerate(lst)))
            lst=['a','b','c','d','e']
            print(list(enumerate(lst,start=-40)))
            lst=['a','b','c','d','e']
            print(list(enumerate(lst,start=46)))
            lst=[('a',4),'b','c',10,'e']
            print(list(enumerate(lst)))
            print(list(enumerate([])))
            print(list(enumerate([], start=10)))
            """)

    def test_enumerate_invalid_start_args(self):
        self.assertCodeExecution("""
            try:
                print(list(enumerate(['a','b','c'], start=None)))
            except TypeError as err:
                print(err)
            try:
                print(list(enumerate(['a','b','c'], start=1.5)))
            except TypeError as err:
                print(err)
            try:
                print(list(enumerate(['a','b','c'], start="start_string")))
            except TypeError as err:
                print(err)
            """)

    def test_enumerate_invalid_iterable(self):
        self.assertCodeExecution("""
            try:
                num=10
                print(list(enumerate(num, start=10)))
            except TypeError as err:
                print(err)
            try:
                print(list(enumerate()))
            except TypeError as err:
                print(err)
            """)


class BuiltinEnumerateFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["enumerate"]

    not_implemented = [
        'test_bytearray',
        'test_bytes',
        'test_dict',
        'test_frozenset',
        'test_list',
        'test_range',
        'test_set',
        'test_str',
        'test_tuple',
    ]
