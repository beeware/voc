from unittest import expectedFailure

from ..utils import TranspileTestCase


class ExceptionTests(TranspileTestCase):

    def test_raise(self):
        # Caught exception
        self.assertCodeExecution("""
            raise KeyError("This is the name")
            """)

    def test_raise_without_any_params(self):
        self.assertCodeExecution("""
            raise ValueError()
        """)

    def test_raise_by_classname(self):
        self.assertCodeExecution("""
            raise ValueError
        """)

    def test_raise_catch(self):
        self.assertCodeExecution("""
            try:
                raise KeyError("This is the name")
            except KeyError:
                print("Got a Key Error")
            print('Done.')
            """)
