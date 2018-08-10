from unittest import expectedFailure

from .. utils import TranspileTestCase


class ObjectTests(TranspileTestCase):
    @expectedFailure
    def test_setitem(self):
        self.assertCodeExecution("""
            class MyClass:
                def __setitem__(self, key, item):
                    print("In __setitem__")

            obj = MyClass()
            obj[0] = 0
            """)

    def test_getitem(self):
        self.assertCodeExecution("""
            class MyClass:
                def __getitem__(self, key):
                    print("In __getitem__")

            obj = MyClass()
            print(obj[0])
            """)
