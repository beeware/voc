from unittest import expectedFailure

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

    @expectedFailure
    def test_closure(self):
        self.assertCodeExecution("""
            def myfunc(value):
                print(value * 3)

                def myinner(value2):
                    print(value2 * value)
                    return value2 + 6

                print("inner value =", myinner(10))
                return value + 5

            print("outer =", myfunc(5))
            print('Done.')
            """)

    def test_default_args(self):
        self.assertCodeExecution("""
            def myfunc(x, y=1, z=2):
                print("x =", x)
                print("y =", y)
                print("z =", z)

            myfunc(37)
            print('Done.')
            """, run_in_function=False)

    def test_override_some_default_args(self):
        self.assertCodeExecution("""
            def myfunc(x, y=1, z=2):
                print("x =", x)
                print("y =", y)
                print("z =", z)

            myfunc(37, 42)
            print('Done.')
            """, run_in_function=False)

    def test_overide_all_default_args(self):
        self.assertCodeExecution("""
            def myfunc(x, y=1, z=2):
                print("x =", x)
                print("y =", y)
                print("z =", z)

            myfunc(37, 42, 99)
            print('Done.')
            """, run_in_function=False)

    def test_use_kwargs(self):
        self.assertCodeExecution("""
            def myfunc(x, y=1, z=2):
                print("x =", x)
                print("y =", y)
                print("z =", z)

            myfunc(37, y=42)
            print('Done.')
            """, run_in_function=False)

    def test_use_kwargs_non_sequential(self):
        self.assertCodeExecution("""
            def myfunc(x, y=1, z=2):
                print("x =", x)
                print("y =", y)
                print("z =", z)

            myfunc(37, z=42)
            print('Done.')
            """, run_in_function=False)

    def test_use_all_kwargs(self):
        self.assertCodeExecution("""
            def myfunc(x, y=1, z=2):
                print("x =", x)
                print("y =", y)
                print("z =", z)

            myfunc(x=37, y=42, z=99)
            print('Done.')
            """, run_in_function=False)

    def test_use_all_kwargs_different_order(self):
        self.assertCodeExecution("""
            def myfunc(x, y=1, z=2):
                print("x =", x)
                print("y =", y)
                print("z =", z)

            myfunc(z=99, y=42, x=37)
            print('Done.')
            """, run_in_function=False)

    def test_call_function_with_var_args(self):
        self.assertCodeExecution("""
                def myfunc(*args):
                    print(args)
                    return args[0]

                print("first arg =", myfunc(1, 2, 3, 4, 5))
                print('Done.')
                """, run_in_function=False)

    def test_call_function_with_kw(self):
        self.assertCodeExecution("""
            def myfunc(**kwargs):
                print(kwargs['first'] * 3)
                print(kwargs['second'] * 3)

                return kwargs['first'] + kwargs['second']

            print("values sum =", myfunc(first=1, second=2))
            print('Done.')
            """, run_in_function=False)

    def test_call_function_kw(self):
        self.assertCodeExecution("""
            def myfunc(**kwargs):
                print(kwargs['first'] * 3)
                print(kwargs['second'] * 3)

                return kwargs['first'] + kwargs['second']

            values = {'first': 1, 'second': 2}
            print("values sum =", myfunc(**values))
            print('Done.')
            """, run_in_function=False)

    def test_call_function_var_kw(self):
        self.assertCodeExecution("""
            def myfunc(*args, **kwargs):
                print(kwargs['first'] * 3)
                print(kwargs['second'] * 3)
                print(args)

                return kwargs['first'] + kwargs['second']

            values_tuple = (1, 2, 3, 4)
            values_dict = {'first': 1, 'second': 2}
            print("values sum =", myfunc(*values_tuple, **values_dict))
            print('Done.')
            """, run_in_function=False)

    def test_call_function_var(self):
        self.assertCodeExecution("""
                def myfunc(*args):
                    print(args)

                    return len(args)

                values_tuple = (1, 2, 3, 4)
                print("values count =", myfunc(*values_tuple))
                print('Done.')
                """, run_in_function=False)
