from .utils import TranspileTestCase


class ListTests(TranspileTestCase):
    def test_creation(self):
        self.assertCode("""
            x = [1, 2, 3, 4, 5]
            print(x)
            """)

    def test_getitem(self):
        # Simple positive index
        self.assertCode("""
            x = [1, 2, 3, 4, 5]
            print(x[2])
            """)

        # Simple negative index
        self.assertCode("""
            x = [1, 2, 3, 4, 5]
            print(x[-2])
            """)

        # Positive index out of range
        self.assertCodeOutput("""
            x = [1, 2, 3, 4, 5]
            print(x[10])
            """, """
            Exception in thread "main" java.lang.ExceptionInInitializerError
            Caused by: org.python.exceptions.IndexError: list index out of range
                at org.python.types.List.__getitem__(List.java:100)
                at org.python.types.List.__getitem__(List.java:85)
                at org.pybee.test.<clinit>(test.py:2)
            """)

        # Negative index out of range
        self.assertCodeOutput("""
            x = [1, 2, 3, 4, 5]
            print(x[-10])
            """, """
            Exception in thread "main" java.lang.ExceptionInInitializerError
            Caused by: org.python.exceptions.IndexError: list index out of range
                at org.python.types.List.__getitem__(List.java:94)
                at org.python.types.List.__getitem__(List.java:85)
                at org.pybee.test.<clinit>(test.py:2)
            """)

    # def test_list_comprehensions(self):
    #     self.assertCode("""
    #         x = [1, 2, 3]
    #         y = [v**2 for v in x]
    #         print(y)
    #         """)
