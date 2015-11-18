from .. utils import TranspileTestCase


class RangeTests(TranspileTestCase):
    def test_creation(self):
        self.assertCodeExecution("""
            x = range(0, 5)
            print("x[0] = ", x[0])
            print("x[1] = ", x[1])
            print("x[3] = ", x[3])
            print("x[-1] = ", x[-1])
            print("x[5] = ", x[5])
            """)

    def test_step(self):
        self.assertCodeExecution("""
            x = range(0, 5, 2)
            print("x[0] = ", x[0])
            print("x[1] = ", x[1])
            print("x[3] = ", x[3])
            print("x[-1] = ", x[-1])
            print("x[5] = ", x[5])
            """)
