from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class MaxTests(TranspileTestCase):

    def test_list(self):
        self.assertCodeExecution("""
            try:
                # print(max([]))
                print(max([1, 2, 13, 8, 5, 3]))
                print(max(["Kirk", "Scotty", "Bones", "Spock", "Sulu"]))
                print(max([3.61, 4.41, 3.14159, 1.618]))
            except Exception as e:
                print(e)
            """, run_in_function=False)

    def test_str(self):
        self.assertCodeExecution("""
            try:
                print(max("Alpha", "Scotty", "Bones", "Spock", "Kirk"))
                print(max('Han Solo'))
                print(max('A', 'B', 'a', 'b'))
            except Exception as e:
                print(e)
            """, run_in_function=False)

    def test_tuple(self):
        self.assertCodeExecution("""
            try:
                print(max((1, 5), (2, 4), (12, 14)))
                print(max(("ackbar", "balrog"), ("klingon", "ewoks"), ("zalthor", "zathura")))
                print(max((1, 4), (1, 2)))
            except Exception as e:
                print(e)
            """, run_in_function=False)

    def test_max(self):
        self.assertCodeExecution("""
            try:
                print(max(1, 5, 3, 2, 4, 9, 12))
                print(max("Pen", "Pineapple", "Apple", "Pen"))
                print(max("foo", "bar", "other"))
                # print(max("foo", "bar", 1729))
            except Exception as e:
                print(e)
            """, run_in_function=False)


class BuiltinMaxFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["max"]

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
        'test_None',
        'test_NotImplemented',
        'test_range',
        'test_set',
        'test_slice',
        'test_str',
        'test_tuple'
    ]
