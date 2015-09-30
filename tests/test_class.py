from .utils import TranspileTestCase


class ClassTests(TranspileTestCase):
    def test_simple(self):
        self.assertCode("""
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
            """)
