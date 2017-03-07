from .. utils import TranspileTestCase


class IsinstanceTests(TranspileTestCase):
    def test_no_args(self):
        self.assertCodeExecution("""
            try:
                print(isinstance())
            except TypeError as err:
                print(err)
            """, run_in_function=False)

    def test_one_arg(self):
        self.assertCodeExecution("""
            try:
                print(isinstance(123))
            except TypeError as err:
                print(err)
            """, run_in_function=False)

    def test_non_tuple_second_arg(self):
        self.assertCodeExecution("""
            try:
                print(isinstance(123, [int, float]))
            except TypeError as err:
                print(err)
            """, run_in_function=False)

    def test_single_class(self):
        self.assertCodeExecution("""
            class MyClass1:
                pass

            class MyClass2:
                pass

            obj = MyClass1()

            print(isinstance(obj, MyClass1))
            print(isinstance(obj, MyClass2))
            """, run_in_function=False)

    def test_multiple_classes(self):
        self.assertCodeExecution("""
            class MyClass1:
                pass

            class MyClass2:
                pass

            obj = MyClass1()

            print(isinstance(obj, (MyClass1, MyClass2)))
            """, run_in_function=False)

    def test_parent(self):
        self.assertCodeExecution("""
            class MyClass1:
                pass

            class MyClass2(MyClass1):
                pass

            obj = MyClass2()

            print(isinstance(obj, MyClass1))
            print(isinstance(obj, MyClass2))
            """, run_in_function=False)

    def test_grandparent(self):
        self.assertCodeExecution("""
            class MyClass1:
                pass

            class MyClass2(MyClass1):
                pass

            class MyClass3(MyClass2):
                pass

            obj = MyClass3()

            print(isinstance(obj, MyClass1))
            print(isinstance(obj, MyClass2))
            print(isinstance(obj, MyClass3))
            """, run_in_function=False)

    def test_types(self):
        self.assertCodeExecution("""
            print(isinstance(123, int))
            print(isinstance(123, str))
            print(isinstance(123, float))

            print(isinstance("asdf", int))
            print(isinstance("asdf", str))
            print(isinstance("asdf", float))

            print(isinstance(123.45, int))
            print(isinstance(123.45, str))
            print(isinstance(123.45, float))

            print(isinstance(123, (int, float)))
            print(isinstance("asdf", (int, float)))
            print(isinstance(123.45, (int, float)))
            """, run_in_function=False)
