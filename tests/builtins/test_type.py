from unittest import expectedFailure

from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class TypeTests(TranspileTestCase):

    @expectedFailure
    def test_dynamic_class_definitions_leak_state(self):
        self.assertCodeExecution("""
            my_class_obj = type("MyClass", (object,), {})
            print("my_class_obj: ", my_class_obj)

            obj = object
            print("obj: ", object)

            dynamic_obj = type("object", (object,), {})
            print("dynamic_obj: ", dynamic_obj)

            # Check state leak
            print("my_class_obj: ", my_class_obj)
            print("obj: ", obj)
        """)


class BuiltinTypeFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["type"]

    not_implemented = [
    ]
