import unittest

from .utils import adjust, cleanse_java, cleanse_python


class AdjustTests(unittest.TestCase):
    def assertEqualOutput(self, actual, expected):
        self.assertEqual(adjust(actual), adjust(expected))

    def test_adjust(self):
        "Test input can be stripped of leading spaces."
        self.assertEqual("""for i in range(0, 10):
    print('hello, world')
print('Done.')
""", adjust("""
            for i in range(0, 10):
                print('hello, world')
            print('Done.')
        """))

    def test_adjust_no_leading_space(self):
        self.assertEqual("""for i in range(0, 10):
    print('hello, world')
print('Done.')
""", adjust("""for i in range(0, 10):
    print('hello, world')
print('Done.')
"""))


class JavaNormalizationTests(unittest.TestCase):
    def assertNormalized(self, actual, expected):
        self.assertEqual(cleanse_java(adjust(actual)), adjust(expected))

    def test_no_exception(self):
        self.assertNormalized(
            """
            Hello, world.
            """,
            """
            Hello, world.
            """
        )

    def test_exception_in_clinit(self):
        self.assertNormalized(
            """
            Exception in thread "main" java.lang.ExceptionInInitializerError
            Caused by: org.python.exceptions.IndexError: list index out of range
                at org.python.types.List.__getitem__(List.java:100)
                at org.python.types.List.__getitem__(List.java:85)
                at python.test.<clinit>(test.py:2)
            """,
            """
            ### EXCEPTION ###
            IndexError: list index out of range
            """
        )

    def test_exception_in_clinit_after_output(self):
        self.assertNormalized(
            """
            Hello, world.
            Exception in thread "main" java.lang.ExceptionInInitializerError
            Caused by: org.python.exceptions.IndexError: list index out of range
                at org.python.types.List.__getitem__(List.java:100)
                at org.python.types.List.__getitem__(List.java:85)
                at python.test.<clinit>(test.py:2)
            """,
            """
            Hello, world.
            ### EXCEPTION ###
            IndexError: list index out of range
            """
        )

    def test_exception_in_method(self):
        self.assertNormalized(
            """
            Exception in thread "main" org.python.exceptions.IndexError: list index out of range
                at org.python.types.List.__getitem__(List.java:100)
                at org.python.types.List.__getitem__(List.java:85)
                at python.test.main(test.py:3)
            """,
            """
            ### EXCEPTION ###
            IndexError: list index out of range
            """
        )

    def test_exception_in_method_after_output(self):
        self.assertNormalized(
            """
            Hello, world.
            Exception in thread "main" org.python.exceptions.IndexError: list index out of range
                at org.python.types.List.__getitem__(List.java:100)
                at org.python.types.List.__getitem__(List.java:85)
                at python.test.main(test.py:3)
            """,
            """
            Hello, world.
            ### EXCEPTION ###
            IndexError: list index out of range
            """
        )

    def test_nested_exception(self):
        self.maxDiff = None
        self.assertNormalized(
            """
            Do final cleanup
            org.python.exceptions.ValueError: invalid literal for int() with base 10: 'asdf'
                at org.python.types.Str.__int__(Str.java:44)
                at org.Python.int_cast(Python.java:680)
                at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
                at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
                at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
                at java.lang.reflect.Method.invoke(Method.java:606)
                at org.python.types.Function.invoke(Function.java:93)
                at python.example.foo(example.py:81)
                at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
                at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
                at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
                at java.lang.reflect.Method.invoke(Method.java:606)
                at org.python.types.Method.invoke(Method.java:45)
                at python.example.<clinit>(example.py:87)
            Exception in thread "main" java.lang.ExceptionInInitializerError
            Caused by: org.python.exceptions.ValueError: invalid literal for int() with base 10: 'asdf'
                at org.python.types.Str.__int__(Str.java:44)
                at org.Python.int_cast(Python.java:680)
                at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
                at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
                at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
                at java.lang.reflect.Method.invoke(Method.java:606)
                at org.python.types.Function.invoke(Function.java:93)
                at python.example.foo(example.py:81)
                at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
                at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
                at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
                at java.lang.reflect.Method.invoke(Method.java:606)
                at org.python.types.Method.invoke(Method.java:45)
                at python.example.<clinit>(example.py:87)
            """,
            """
            Do final cleanup
            ### EXCEPTION ###
            ValueError: invalid literal for int() with base 10: 'asdf'
            """
        )

    def test_float(self):
        self.assertNormalized('7.950899459780156E-6', '7.950899459780156e-6')


class PythonNormalizationTests(unittest.TestCase):
    def assertNormalized(self, actual, expected):
        self.assertEqual(cleanse_python(adjust(actual)), adjust(expected))

    def test_no_exception(self):
        self.assertNormalized(
            """
            Hello, world.
            """,
            """
            Hello, world.
            """
        )

    def test_exception(self):
        self.assertNormalized(
            """
            Traceback (most recent call last):
              File "test.py", line 3, in <module>
                print(x & y)
            TypeError: unsupported operand type(s) for &: 'float' and 'bool'
            """,
            """
            ### EXCEPTION ###
            TypeError: unsupported operand type(s) for &: 'float' and 'bool'
            """
        )

    def test_exception_with_other_text(self):
        self.assertNormalized(
            """
            Hello, world.
            Traceback (most recent call last):
              File "test.py", line 3, in <module>
                print(x & y)
            TypeError: unsupported operand type(s) for &: 'float' and 'bool'
            """,
            """
            Hello, world.
            ### EXCEPTION ###
            TypeError: unsupported operand type(s) for &: 'float' and 'bool'
            """
        )

    def test_float(self):
        self.assertNormalized('7.950899459780156e-06', '7.950899459780156e-6')
