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


class JavanNormalizationTests(unittest.TestCase):
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
                at org.pybee.test.<clinit>(test.py:2)
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
                at org.pybee.test.<clinit>(test.py:2)
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
                at org.pybee.test.main(test.py:3)
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
                at org.pybee.test.main(test.py:3)
            """,
            """
            Hello, world.
            ### EXCEPTION ###
            IndexError: list index out of range
            """
        )

    def test_float(self):
        self.assertNormalized('7.950899459780156E-6', '7.950899459780156e-6')


class PythonNormalizationTests(unittest.TestCase):
    def assertNormalized(self, actual, expected):
        self.assertEqual(cleanse_python(adjust(actual)), adjust(expected))

    def assert_no_exception(self):
        self.assertNormalized(
            """
            Hello, world.
            """,
            """
            Hello, world.
            """
        )

    def assert_exception(self):
        self.assertNormalized(
            """
            Traceback (most recent call last):
              File "/Users/rkm/projects/beeware/voc/tests/utils.py", line 107, in assertCodeExecution
                exec(code, {}, {})
              File "<string>", line 2, in <module>
            IndexError: list index out of range
            """,
            """
            ### EXCEPTION ###
            IndexError: list index out of range
            """
        )

    def assert_exception_with_other_text(self):
        self.assertNormalized(
            """
            Hello, world.
            Traceback (most recent call last):
              File "/Users/rkm/projects/beeware/voc/tests/utils.py", line 107, in assertCodeExecution
                exec(code, {}, {})
              File "<string>", line 2, in <module>
            IndexError: list index out of range
            """,
            """
            Hello, world.
            ### EXCEPTION ###
            IndexError: list index out of range
            """
        )

    def test_float(self):
        self.assertNormalized('7.950899459780156e-06', '7.950899459780156e-6')
