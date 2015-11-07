from ..utils import TranspileTestCase


class FunctionTests(TranspileTestCase):
    def test_function(self):
        self.assertCodeExecution("""
            def myfunc(value):
                print(value * 3)
                return value + 5

            print("value =", myfunc(5))
            print('Done.')
            """)

    def test_void_function(self):
        self.assertCodeExecution("""
            def myfunc(value):
                print(value * 3)

            myfunc(5)
            print('Done.')
            """)

    def test_mainline(self):
        self.assertCodeExecution("""
            if __name__ == '__main__':
                print("Hello, world")
            """, run_in_function=False)

    def test_inner_function(self):
        self.assertCodeExecution("""
            def myfunc(value):
                print(value * 3)

                def myinner(value2):
                    print(value2 * 4)
                    return value2 + 6

                print("inner value =", myinner(10))
                return value + 5

            print("outer =", myfunc(5))
            print('Done.')
            """, run_in_function=False)


    # def test_closure(self):
    #     self.assertCodeExecution("""
    #         def myfunc(value):
    #             print(value * 3)

    #             def myinner(value2):
    #                 print(value2 * value)
    #                 return value2 + 6

    #             print("inner value =", myinner(10))
    #             return value + 5

    #         print("outer =", myfunc(5))
    #         print('Done.')
    #         """)
