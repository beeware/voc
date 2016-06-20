from unittest import expectedFailure

from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class SumTests(TranspileTestCase):
    def test_sum_list(self):
        self.assertCodeExecution("""
            print(sum([1, 2, 3, 4, 5, 6, 7]))
        """)

    def test_sum_tuple(self):
        self.assertCodeExecution("""
            print(sum((1, 2, 3, 4, 5, 6, 7)))
        """)

    def test_sum_iterator(self):
        self.assertCodeExecution("""
            i = iter([1, 2])
            print(sum(i))
            print(sum(i))
        """)

    @expectedFailure  # + not defined on float/float yet.
    def test_sum_mix_floats_and_ints(self):
        self.assertCodeExecution("""
            print(sum([1, 1.414, 2, 3.14159]))
        """)


class BuiltinSumFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["sum"]

    not_implemented = [
        'test_bytearray',
        'test_bytes',
        'test_class',
        'test_complex',
        'test_dict',
        'test_frozenset',
        'test_set',
        'test_slice',
        'test_str',
    ]
