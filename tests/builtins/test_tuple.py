from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class TupleTests(TranspileTestCase):
    def test_tuple_constructor(self):
        self.assertCodeExecution("""
            #No args
            print(tuple())

            #List arg
            print(tuple([1,2,3]))
            """)

        self.assertCodeExecution("""
            #more than one arg throws exception
            print(tuple(1,2))
            """, exits_early=True)


class BuiltinTupleFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["tuple"]

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
