from ..utils import TranspileTestCase


class ReturnTests(TranspileTestCase):
    def test_return_methods(self):
        # Empty return
        self.assertCodeExecution("""
            def m():
                print('before return')
                return
                print('after return')

            print(m())
        """)

        # Single return
        self.assertCodeExecution("""
            def m():
                print('before return')
                return 1
                print('after return')

            print(m() + 1)
        """)

        # Multiple return
        self.assertCodeExecution("""
            def m():
                print('before return')
                return 1, 2
                print('after return')

            print(m())
        """)
