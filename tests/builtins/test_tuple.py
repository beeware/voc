from unittest import expectedFailure

from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class TupleTests(TranspileTestCase):

    @expectedFailure
    def test_bad_tuple(self):
        self.assertCodeExecution("""
            try:
                print(tuple(0, 1))
            except TypeError as err:
                print(err)

            try:
                print(tuple(0))
            except TypeError as err:
                print(err)
        """)


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
