from ..utils import TranspileTestCase


class ReturnTests(TranspileTestCase):
    def test_return_methods(self):
        # Empty return
        self.assertCodeExecution("""
            def m():
                print('haha')
                return
                print('haha')

            print(m())
        """)

        # Single return
        self.assertCodeExecution("""
            def m():
                print('haha')
                return 1
                print('haha')

            print(m() + 1)
        """)

        # Multiple return
        self.assertCodeExecution("""
            def m():
                print('haha')
                return 1, 2
                print('haha')

            print(m())
        """)

