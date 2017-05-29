from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class IssubclassTests(TranspileTestCase):
    def test_no_args(self):
        self.assertCodeExecution("""
            try:
                print(issubclass())
            except TypeError as err:
                print(err)
            """, run_in_function=False)

    def test_one_arg(self):
        self.assertCodeExecution("""
            try:
                print(issubclass(123))
            except TypeError as err:
                print(err)
            """, run_in_function=False)

    def test_non_class_first_arg(self):
        self.assertCodeExecution("""
            try:
                print(issubclass(0, 0))
            except TypeError as err:
                print(err)
            """, run_in_function=False)

    def test_non_tuple_second_arg(self):
        self.assertCodeExecution("""
            class MyClass1:
                pass

            try:
                print(issubclass(MyClass1, [int, float]))
            except TypeError as err:
                print(err)
            """, run_in_function=False)

    def test_single_class(self):
        self.assertCodeExecution("""
            class MyClass1:
                pass

            class MyClass2:
                pass

            print(issubclass(MyClass1, MyClass1))
            print(issubclass(MyClass1, MyClass2))
            """, run_in_function=False)

    def test_multiple_classes(self):
        self.assertCodeExecution("""
            class MyClass1:
                pass

            class MyClass2:
                pass

            print(issubclass(MyClass1, (MyClass1, MyClass2)))
            """, run_in_function=False)

    def test_parent(self):
        self.assertCodeExecution("""
            class MyClass1:
                pass

            class MyClass2(MyClass1):
                pass

            print(issubclass(MyClass2, MyClass1))
            print(issubclass(MyClass1, MyClass2))
            """, run_in_function=False)

    def test_grandparent(self):
        self.assertCodeExecution("""
            class MyClass1:
                pass

            class MyClass2(MyClass1):
                pass

            class MyClass3(MyClass2):
                pass

            print(issubclass(MyClass2, MyClass1))
            print(issubclass(MyClass3, MyClass2))
            print(issubclass(MyClass3, MyClass1))
            """, run_in_function=False)


class BuiltinIssubclassFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["issubclass"]

    not_implemented = [
    ]
