from unittest import expectedFailure

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

    @expectedFailure
    def test_key(self):
        self.assertCodeExecution("""
            # key applied over args
            print(min(51, 42, 33, 24, key=lambda v: v % 10))

            # key applied over iterable
            print(min([51, 42, 33, 24], key=lambda v: v % 10))
            """)


class BuiltinMinFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["min"]

    not_implemented = [
        'test_bytearray',
        'test_bytes',
        'test_frozenset',
        'test_set',
        'test_tuple',
    ]
