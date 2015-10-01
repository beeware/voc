from .utils import TranspileTestCase


class ListTests(TranspileTestCase):
    def test_creation(self):
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print(x)
            """)

    def test_getitem(self):
        # Simple positive index
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print(x[2])
            """)

        # Simple negative index
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print(x[-2])
            """)

        # Positive index out of range
        self.assertCodeExecution("""
            if __name__ == '__main__':
                x = [1, 2, 3, 4, 5]
                print(x[10])
            """)

        # Negative index out of range
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print(x[-10])
            """)

    # def test_list_comprehensions(self):
    #     self.assertCodeExecution("""
    #         x = [1, 2, 3]
    #         y = [v**2 for v in x]
    #         print(y)
    #         """)
