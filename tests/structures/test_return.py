from unittest import expectedFailure

from ..utils import TranspileTestCase


class ReturnTests(TranspileTestCase):
    def test_return_methods(self):
        # Empty return
        self.assertCodeExecution("""
            def m():
                return

            print(m())
        """)

        # Single return
        self.assertCodeExecution("""
            def m():
                return 1

            print(m() + 1)
        """)

        # Multiple return
        self.assertCodeExecution("""
            def m():
                return 1, 2

            print(m())
        """)
