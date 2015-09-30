from .utils import TranspileTestCase


class FunctionTests(TranspileTestCase):
    def test_function(self):
        self.assertCode("""
            def myfunc(value):
                print(value * 3)
                return value + 5

            myfunc(5)
            print('Done.')
            """)

    def test_void_function(self):
        self.assertCode("""
            def myfunc(value):
                print(value * 3)

            myfunc(5)
            print('Done.')
            """)
