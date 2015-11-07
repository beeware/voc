from ..utils import TranspileTestCase


class ClassTests(TranspileTestCase):
    def test_minimal(self):
        self.assertCodeExecution("""
            class MyClass:
                pass

            obj = MyClass()

            print('Done.')
            """, run_in_function=False)

    def test_simple(self):
        self.assertCodeExecution("""
            class MyClass:
                def __init__(self, val):
                    print("VAL: ", val)
                    self.value = val

                def stuff(self, delta):
                    print("DELTA: ", delta)
                    return self.value + delta

            obj = MyClass(4)
            obj.stuff(5)

            print('Done.')
            """, run_in_function=False)
