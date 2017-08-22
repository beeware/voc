from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class MinTests(TranspileTestCase):
    def test_args(self):
        self.assertCodeExecution("""
            try:
                min()
            except TypeError:
                print("Threw an error as expected")

            # Single integer
            try:
                min(4)
            except TypeError:
                print("Threw an error as expected")

            # Multiple integers
            print(min(1, 5, 2, 4))

            # Mixed types
            print(min(2, 5.0, True))
            print(min(5.0, 2, True))
            print(min(True, 5.0, 2))

            # String (an iterable)
            print(min("Hello World"))

            # Multiple strings
            print(min("Hello World", "Goodbye World"))
            """)

    def test_iterable(self):
        self.assertCodeExecution("""
            # Empty iterable
            try:
                min([])
            except ValueError:
                print("Threw an error as expected")

            # Single iterable argument
            print(min([1, 5, 2, 4]))

            # Multiple iterables
            print(min([1, 6], [1, 5, 2, 4]))
            """)

    def test_default(self):
        self.assertCodeExecution("""
            # Empty iterable
            print(min([], default=42))

            # Single iterable argument
            print(min([1, 5, 2, 4], default=42))

            # Multiple iterables
            try:
                print(min([1, 6], [1, 5, 2, 4], default=42))
            except TypeError:
                print("Threw an error as expected")
            """)

    def test_key(self):
        self.assertCodeExecution("""
            # key applied over args
            print(min(51, 42, 33, 24, key=lambda v: v % 10))

            # key applied over iterable
            print(min([51, 42, 33, 24], key=lambda v: v % 10))

            print(min([(2, 4), (5, 0), (4, 0), (9, 3)], key=lambda t: t[1]))
            """)


class BuiltinMinFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["min"]

    not_implemented = [
        'test_tuple',
    ]
