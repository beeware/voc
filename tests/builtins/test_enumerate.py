from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class EnumerateTests(TranspileTestCase):
    def test_enumerate(self):
        self.assertCodeExecution("""
            lst=['a','b','c','d','e']
            print(list(enumerate(lst)))
            """)

        self.assertCodeExecution("""
            lst=['a','b','c','d','e']
            print(list(enumerate(lst,start=-40)))
            """)

        self.assertCodeExecution("""
            lst=['a','b','c','d','e']
            print(list(enumerate(lst,start=46)))
            """)

        self.assertCodeExecution("""
            lst=[('a',4),'b','c',10,'e']
            print(list(enumerate(lst)))
            """)

    def test_enumerate_invalid_start_args(self):
        self.assertCodeExecution("""
            print(list(enumerate(['a','b','c'], start=None)))
            """, exits_early=True)
        self.assertCodeExecution("""
            print(list(enumerate(['a','b','c'], start=1.5)))
            """, exits_early=True)
        self.assertCodeExecution("""
            print(list(enumerate(['a','b','c'], start="start_string")))
            """, exits_early=True)
            
    def test_enumerate_invalid_iterable(self):
        self.assertCodeExecution("""
            num=10
            print(list(enumerate(num, start=10)))
            """, exits_early=True)
        self.assertCodeExecution("""
            st="IterateMe"
            print(list(enumerate(st)))
            """, exits_early=True)
            

class BuiltinEnumerateFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["enumerate"]

    not_implemented = [
        'test_bool',
        'test_bytearray',
        'test_bytes',
        'test_class',
        'test_complex',
        'test_dict',
        'test_float',
        'test_frozenset',
        'test_int',
        'test_list',
        'test_None',
        'test_NotImplemented',
        'test_range',
        'test_set',
        'test_slice',
        'test_str',
        'test_tuple',
    ]
