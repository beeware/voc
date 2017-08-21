from ..utils import TranspileTestCase


class LambdaTests(TranspileTestCase):
    def test_lambda(self):
        self.assertCodeExecution("""
            f = lambda : 42
            print(f())

            g = lambda x : x
            print(g(10))

            print((lambda x: x + '!!!')('hello'))

            print((lambda x='something': x + '!!!')('hello'))

            print((lambda x: x + '!!!')(x='hello'))

            """)

    def test_lambda_kwonly(self):
        self.assertCodeExecution("""
            print((lambda *,x='something': x + '!!!')())
            """)


class FunctionTests(TranspileTestCase):
    def test_function(self):
        self.assertCodeExecution("""
            def myfunc(value):
                print(value * 3)
                return value + 5

            print("value =", myfunc(5))
            """)

    def test_function_name_attribute(self):
        self.assertCodeExecution("""
            def myfunc():
                def otherfunc():
                    pass
                print(otherfunc.__name__)

            print(myfunc.__name__)
            myfunc()
            """)

    def test_noargs_function(self):
        self.assertCodeExecution("""
            def myfunc():
                print('Hello')
                return 5

            print("value =", myfunc())
            """)

    def test_void_function(self):
        self.assertCodeExecution("""
            def myfunc(value):
                print(value * 3)

            myfunc(5)
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
            """, run_in_function=False)

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
            """)

    def test_default_args(self):
        self.assertCodeExecution("""
            def myfunc(x, y=1, z=2):
                print("x =", x)
                print("y =", y)
                print("z =", z)

            myfunc(37)
            """, run_in_function=False)

    def test_override_some_default_args(self):
        self.assertCodeExecution("""
            def myfunc(x, y=1, z=2):
                print("x =", x)
                print("y =", y)
                print("z =", z)

            myfunc(37, 42)
            """, run_in_function=False)

    def test_overide_all_default_args(self):
        self.assertCodeExecution("""
            def myfunc(x, y=1, z=2):
                print("x =", x)
                print("y =", y)
                print("z =", z)

            myfunc(37, 42, 99)
            """, run_in_function=False)

    def test_use_kwargs(self):
        self.assertCodeExecution("""
            def myfunc(x, y=1, z=2):
                print("x =", x)
                print("y =", y)
                print("z =", z)

            myfunc(37, y=42)
            """, run_in_function=False)

    def test_use_kwargs_non_sequential(self):
        self.assertCodeExecution("""
            def myfunc(x, y=1, z=2):
                print("x =", x)
                print("y =", y)
                print("z =", z)

            myfunc(37, z=42)
            """, run_in_function=False)

    def test_use_all_kwargs(self):
        self.assertCodeExecution("""
            def myfunc(x, y=1, z=2):
                print("x =", x)
                print("y =", y)
                print("z =", z)

            myfunc(x=37, y=42, z=99)
            """, run_in_function=False)

    def test_use_all_kwargs_different_order(self):
        self.assertCodeExecution("""
            def myfunc(x, y=1, z=2):
                print("x =", x)
                print("y =", y)
                print("z =", z)

            myfunc(z=99, y=42, x=37)
            """, run_in_function=False)

    def test_call_function_with_var_args(self):
        self.assertCodeExecution("""
            def myfunc(*args):
                print(args)
                return args[0]

            print("first arg =", myfunc(1, 2, 3, 4, 5))
            """, run_in_function=False)

    def test_call_function_with_kw(self):
        self.assertCodeExecution("""
            def myfunc(**kwargs):
                print(kwargs['first'] * 3)
                print(kwargs['second'] * 3)

                return kwargs['first'] + kwargs['second']

            print("values sum =", myfunc(first=1, second=2))
            """, run_in_function=False)

    def test_call_function_kw(self):
        self.assertCodeExecution("""
            def myfunc(**kwargs):
                print(kwargs['first'] * 3)
                print(kwargs['second'] * 3)

                return kwargs['first'] + kwargs['second']

            values = {'first': 1, 'second': 2}
            print("values sum =", myfunc(**values))
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
            """, run_in_function=False)

    def test_call_function_var(self):
        self.assertCodeExecution("""
            def myfunc(*args):
                print(args)

                return len(args)

            values_tuple = (1, 2, 3, 4)
            print("values count =", myfunc(*values_tuple))
            """, run_in_function=False)

    def test_redefine(self):
        self.assertCodeExecution("""
            def myfunc(value):
                print(value * 3)
                return value + 5

            def myfunc(value):
                print(value * 4)
                return value + 6

            print("value =", myfunc(5))
            """)

    def test_noarg_unexpected_extra_arg(self):
        self.assertCodeExecution("""
            def myfunc():
                pass

            myfunc(5)
            """, exits_early=True)

    def test_noarg_unexpected_extra_several_args(self):
        self.assertCodeExecution("""
            def myfunc():
                return 16

            print(myfunc(1, 2, 3))
            """, exits_early=True)

    def test_unexpected_extra_several_args(self):
        self.assertCodeExecution("""
            def myfunc(a):
                return 16

            print(myfunc(1, 2, 3))
            """, exits_early=True)

    def test_multiple_args_unexpected_extra_several_args(self):
        self.assertCodeExecution("""
            def myfunc(a, b):
                return 16

            print(myfunc(1, 2, 3))
            """, exits_early=True)

    def test_missing_sole_arg(self):
        self.assertCodeExecution("""
            def myfunc(a):
                return 16

            print(myfunc())
            """, exits_early=True)

    def test_missing_args_more_args(self):
        self.assertCodeExecution("""
            def otherfunc(a, b, c, d, e, f=3):
                return 'ok'

            print(otherfunc(1))
            """, exits_early=True)

    def test_missing_args_with_varargs(self):
        self.assertCodeExecution("""
            def myfunc(a, b, *c, d=3):
                return 'ok'

            print(myfunc(1))
            """, exits_early=True)

    def test_a_method_missing_args(self):
        self.assertCodeExecution("""
            class MyClass:
                def a_method(self, a, b, c):
                    return 16

            i = MyClass()
            print(i.a_method())
            """, exits_early=True)

    def test_function_kwonly(self):
        self.assertCodeExecution("""
            def myfunc(*,x=100):
                return x

            print (myfunc())
            """)

    def test_function_try_except_return_no_exception(self):
        self.assertCodeExecution("""
            def myfunc(x):
                try:
                    return x
                except NameError:
                    return None

            print(myfunc(10))
            """)

    def test_function_try_except_return_caught_exception(self):
        self.assertCodeExecution("""
            def myfunc(x):
                try:
                    return y
                except NameError:
                    return x

            print(myfunc(10))
            """)

    def test_function_try_except_return_uncaught_exception(self):
        self.assertCodeExecution("""
            def myfunc(x):
                try:
                    return z
                except IndexError:
                    return x

            print(myfunc(10))
            """, exits_early=True)
