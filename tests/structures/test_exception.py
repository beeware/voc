from unittest import expectedFailure

from ..utils import TranspileTestCase


class ExceptionTests(TranspileTestCase):

    def test_raise(self):
        # Caught exception
        self.assertCodeExecution("""
            raise KeyError("This is the name")
            print('Done.')
            """, exits_early=True)

    def test_raise_without_any_params(self):
        self.assertCodeExecution("""
            raise ValueError()
            print('Done.')
        """, exits_early=True)

    def test_raise_by_classname(self):
        self.assertCodeExecution("""
            raise ValueError
            print('Done.')
        """, exits_early=True)

    def test_raise_catch(self):
        self.assertCodeExecution("""
            try:
                raise KeyError("This is the name")
                print("No error")
            except KeyError:
                print("Got a Key Error")
            print('Done.')
            """)

    def test_reraise(self):
        self.assertCodeExecution("""
            try:
                raise KeyError("This is the name")
                print("No error")
            except KeyError:
                print("Got error")
                raise
            print('Done.')
            """, exits_early=True)

    def test_reraise_anonymous(self):
        self.assertCodeExecution("""
            try:
                raise KeyError("This is the name")
                print("No error")
            except:
                print("Got error")
                raise
            print('Done.')
            """, exits_early=True)

    def test_reraise_named(self):
        self.assertCodeExecution("""
            try:
                raise KeyError("This is the name")
                print("No error")
            except KeyError as e:
                print("Got error")
                raise
            print('Done.')
            """, exits_early=True)

    def test_raise_custom_exception(self):
        self.assertCodeExecution("""
            class MyException(Exception):
                pass

            try:
                raise MyException()
            except MyException:
                print("Got a custom exception")
            print('Done.')
            """)

    def test_raising_exceptions_multiple_args(self):
        self.assertCodeExecution("""
            for exc in [KeyError, ValueError, TypeError]:
                try:
                    raise exc("one")
                except Exception as e:
                    print(e, e.args)
                try:
                    raise exc("one", 2)
                except Exception as e:
                    print(e, e.args)
        """)

    @expectedFailure
    def test_raise_custom_exception_import_from(self):
        self.assertCodeExecution(
            """
            from example import *

            try:
                raise MyException("This is the exception")
            except MyException:
                print("Got a custom exception")
            print('Done.')
            """,
            extra_code={
                'example':
                    """
                    class MyException(Exception):
                        pass

                    """
            })
