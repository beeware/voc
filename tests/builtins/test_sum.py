from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class SumTests(TranspileTestCase):
    def test_sum_list(self):
        self.assertCodeExecution("""
            print(sum([1, 2, 3, 4, 5, 6, 7]))
            print(sum([[1, 2], [3, 4], [5, 6]], []))
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

    def test_sum_mix_floats_and_ints(self):
        self.assertCodeExecution("""
            print(sum([1, 1.414, 2, 3.14159]))
        """)

    def test_sum_frozenset(self):
        self.assertCodeExecution("""
            print(sum(frozenset([1, 1.414, 2, 3.14159])))
        """)

    def test_sum_set(self):
        self.assertCodeExecution("""
            print(sum({1, 1.414, 2, 3.14159}))
        """)

    def test_sum_dict(self):
        self.assertCodeExecution("""
            print(sum({1: 1.414, 2: 3.14159}))
        """)

    def test_sum_generator_expressions(self):
        self.assertCodeExecution("""
            print(sum(x ** 2 for x in [3, 4]))
        """)


class BuiltinSumFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["sum"]

    not_implemented = [
    ]
