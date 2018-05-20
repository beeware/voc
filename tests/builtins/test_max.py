from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class MaxTests(TranspileTestCase):
    def test_args(self):
        self.assertCodeExecution("""
            try:
                max()
            except TypeError:
                print("Threw an error as expected")

            # Single integer
            try:
                max(4)
            except TypeError:
                print("Threw an error as expected")

            # Multiple integers
            print(max(1, 5, 2, 4))

            # Mixed types
            print(max(2, 5.0, True))
            print(max(5.0, 2, True))
            print(max(True, 5.0, 2))

            # String (an iterable)
            print(max("Hello World"))

            # Multiple strings
            print(max("Hello World", "Goodbye World"))
            """)

    def test_iterable(self):
        self.assertCodeExecution("""
            # Empty iterable
            try:
                max([])
            except ValueError:
                print("Threw an error as expected")

            # Single iterable argument
            print(max([1, 5, 2, 4]))

            # Multiple iterables
            print(max([1, 6], [1, 5, 2, 4]))
            """)

    def test_default(self):
        self.assertCodeExecution("""
            # Empty iterable
            print(max([], default=42))

            # Single iterable argument
            print(max([1, 5, 2, 4], default=42))

            # Multiple iterables
            try:
                print(max([1, 6], [1, 5, 2, 4], default=42))
            except TypeError:
                print("Threw an error as expected")
            """)

    def test_key(self):
        self.assertCodeExecution("""
            # key applied over args
            print(max(51, 42, 33, 24, key=lambda v: v % 10))

            # key applied over iterable
            print(max([51, 42, 33, 24], key=lambda v: v % 10))
            """)


class BuiltinMaxFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["max"]
