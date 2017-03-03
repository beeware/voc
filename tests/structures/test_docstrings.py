from ..utils import TranspileTestCase


class DocstringTests(TranspileTestCase):
    def test_method_docstring(self):
        self.assertCodeExecution("""
            def test():
                "This is the docstring"
                return 3

            print(test())
            print(test.__doc__)
            """)

    def test_naked_string(self):
        self.assertCodeExecution("""
            def test():
                x = 3
                "This is a naked string"
                return x

            print(test())
            print(test.__doc__)
            """)
