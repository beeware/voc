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
            
    #pass


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
