from .utils import TranspileTestCase


class TupleTests(TranspileTestCase):
    def test_creation(self):
        self.assertCode("""
            a = 1
            b = 2
            c = 3
            d = 4
            e = 5
            x = (a, b, c, d, e)
            print(x)
            """)

    def test_const_creation(self):
        self.assertCode("""
            x = (1, 2, 3, 4, 5)
            print(x)
            """)

    def test_const_creation_multitype(self):
        self.assertCode("""
            x = (1, 2.5, "3", True, 5)
            print(x)
            """)

    def test_getitem(self):
        # Simple positive index
        self.assertCode("""
            x = (1, 2, 3, 4, 5)
            print(x[2])
            """)

        # Simple negative index
        self.assertCode("""
            x = (1, 2, 3, 4, 5)
            print(x[-2])
            """)

        # Positive index out of range
        self.assertCodeOutput("""
            x = (1, 2, 3, 4, 5)
            print(x[10])
            """, """
            Exception in thread "main" java.lang.ExceptionInInitializerError
            Caused by: org.python.exceptions.IndexError: tuple index out of range
                at org.python.types.Tuple.__getitem__(Tuple.java:116)
                at org.python.types.Tuple.__getitem__(Tuple.java:101)
                at org.pybee.test.<clinit>(test.py:2)
            """)

        # Negative index out of range
        self.assertCodeOutput("""
            x = (1, 2, 3, 4, 5)
            print(x[-10])
            """, """
            Exception in thread "main" java.lang.ExceptionInInitializerError
            Caused by: org.python.exceptions.IndexError: tuple index out of range
                at org.python.types.Tuple.__getitem__(Tuple.java:110)
                at org.python.types.Tuple.__getitem__(Tuple.java:101)
                at org.pybee.test.<clinit>(test.py:2)
            """)
