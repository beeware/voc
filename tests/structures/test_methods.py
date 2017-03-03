from ..utils import TranspileTestCase


class MethodTests(TranspileTestCase):
    def test_method(self):
        self.assertCodeExecution("""
            class TestObj:
                def myfunc(self, value):
                    print(value * 3)
                    return value + 5

            obj = TestObj()
            print("value =", obj.myfunc(5))
            """)

    def test_noargs_method(self):
        self.assertCodeExecution("""
            class TestObj:
                def myfunc(self, ):
                    print('Hello')
                    return 5

            obj = TestObj()
            print("value =", obj.myfunc())
            """)

    def test_void_method(self):
        self.assertCodeExecution("""
            class TestObj:
                def myfunc(self, value):
                    print(value * 3)

            obj = TestObj()
            obj.myfunc(5)
            """)

    def test_inner_function(self):
        self.assertCodeExecution("""
            class TestObj:
                def myfunc(self, value):
                    print(value * 3)

                    def myinner(value2):
                        print(value2 * 4)
                        return value2 + 6

                    print("inner value =", myinner(10))
                    return value + 5

            obj = TestObj()
            print("outer =", obj.myfunc(5))
            """, run_in_function=False)

    def test_closure(self):
        self.assertCodeExecution("""
            class TestObj:
                def myfunc(self, value):
                    print(value * 3)

                    def myinner(value2):
                        print(value2 * value)
                        return value2 + 6

                    print("inner value =", myinner(10))
                    return value + 5

            obj = TestObj()
            print("outer =", obj.myfunc(5))
            """)

    def test_default_args(self):
        self.assertCodeExecution("""
            class TestObj:
                def myfunc(self, x, y=1, z=2):
                    print("x =", x)
                    print("y =", y)
                    print("z =", z)

            obj = TestObj()
            obj.myfunc(37)
            """, run_in_function=False)

    def test_override_some_default_args(self):
        self.assertCodeExecution("""
            class TestObj:
                def myfunc(self, x, y=1, z=2):
                    print("x =", x)
                    print("y =", y)
                    print("z =", z)

            obj = TestObj()
            obj.myfunc(37, 42)
            """, run_in_function=False)

    def test_overide_all_default_args(self):
        self.assertCodeExecution("""
            class TestObj:
                def myfunc(self, x, y=1, z=2):
                    print("x =", x)
                    print("y =", y)
                    print("z =", z)

            obj = TestObj()
            obj.myfunc(37, 42, 99)
            """, run_in_function=False)

    def test_use_kwargs(self):
        self.assertCodeExecution("""
            class TestObj:
                def myfunc(self, x, y=1, z=2):
                    print("x =", x)
                    print("y =", y)
                    print("z =", z)

            obj = TestObj()
            obj.myfunc(37, y=42)
            """, run_in_function=False)

    def test_use_kwargs_non_sequential(self):
        self.assertCodeExecution("""
            class TestObj:
                def myfunc(self, x, y=1, z=2):
                    print("x =", x)
                    print("y =", y)
                    print("z =", z)

            obj = TestObj()
            obj.myfunc(37, z=42)
            """, run_in_function=False)

    def test_use_all_kwargs(self):
        self.assertCodeExecution("""
            class TestObj:
                def myfunc(self, x, y=1, z=2):
                    print("x =", x)
                    print("y =", y)
                    print("z =", z)

            obj = TestObj()
            obj.myfunc(x=37, y=42, z=99)
            """, run_in_function=False)

    def test_use_all_kwargs_different_order(self):
        self.assertCodeExecution("""
            class TestObj:
                def myfunc(self, x, y=1, z=2):
                    print("x =", x)
                    print("y =", y)
                    print("z =", z)

            obj = TestObj()
            obj.myfunc(z=99, y=42, x=37)
            """, run_in_function=False)

    def test_call_method_with_var_args(self):
        self.assertCodeExecution("""
            class TestObj:
                def myfunc(self, *args):
                    print(args)
                    return args[0]

            obj = TestObj()
            print("first arg =", obj.myfunc(1, 2, 3, 4, 5))
            """, run_in_function=False)

    def test_call_method_with_kw(self):
        self.assertCodeExecution("""
            class TestObj:
                def myfunc(self, **kwargs):
                    print(kwargs['first'] * 3)
                    print(kwargs['second'] * 3)

                    return kwargs['first'] + kwargs['second']

            obj = TestObj()
            print("values sum =", obj.myfunc(first=1, second=2))
            """, run_in_function=False)

    def test_call_method_kw(self):
        self.assertCodeExecution("""
            class TestObj:
                def myfunc(self, **kwargs):
                    print(kwargs['first'] * 3)
                    print(kwargs['second'] * 3)

                    return kwargs['first'] + kwargs['second']

            obj = TestObj()
            values = {'first': 1, 'second': 2}
            print("values sum =", obj.myfunc(**values))
            """, run_in_function=False)

    def test_call_method_var_kw(self):
        self.assertCodeExecution("""
            class TestObj:
                def myfunc(self, *args, **kwargs):
                    print(kwargs['first'] * 3)
                    print(kwargs['second'] * 3)
                    print(args)

                    return kwargs['first'] + kwargs['second']

            obj = TestObj()
            values_tuple = (1, 2, 3, 4)
            values_dict = {'first': 1, 'second': 2}
            print("values sum =", obj.myfunc(*values_tuple, **values_dict))
            """, run_in_function=False)

    def test_call_method_var(self):
        self.assertCodeExecution("""
            class TestObj:
                def myfunc(self, *args):
                    print(args)

                    return len(args)

            obj = TestObj()
            values_tuple = (1, 2, 3, 4)
            print("values count =", obj.myfunc(*values_tuple))
            """, run_in_function=False)
