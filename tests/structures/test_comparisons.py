from ..utils import TranspileTestCase


class ComparisonTests(TranspileTestCase):
    def test_is(self):
        self.assertCodeExecution("""
            x = 1234
            if x is 1234:
                print('True')
            else:
                print('False')
            """)

        self.assertCodeExecution("""
            x = 1234
            if x is 2345:
                print('True')
            else:
                print('False')
            """)

        self.assertCodeExecution("""
            x = None
            if x is None:
                print('True')
            else:
                print('False')
            """)

        self.assertCodeExecution("""
            x = 1234
            if x is None:
                print('True')
            else:
                print('False')
            """)

    def test_is_not(self):
        self.assertCodeExecution("""
            x = 1234
            if x is not 2345:
                print('True')
            else:
                print('False')
            """)

        self.assertCodeExecution("""
            x = 1234
            if x is not 1234:
                print('True')
            else:
                print('False')
            """)

        self.assertCodeExecution("""
            x = 1234
            if x is not None:
                print('True')
            else:
                print('False')
            """)

        self.assertCodeExecution("""
            x = None
            if x is not None:
                print('True')
            else:
                print('False')
            """)

    def test_lt(self):
        self.assertCodeExecution("""
            x = 1
            if x < 5:
                print('True')
            else:
                print('False')
            """)

        self.assertCodeExecution("""
            x = 5
            if x < 5:
                print('True')
            else:
                print('False')
            """)

        self.assertCodeExecution("""
            x = 10
            if x < 5:
                print('True')
            else:
                print('False')
            """)

    def test_le(self):
        self.assertCodeExecution("""
            x = 1
            if x <= 5:
                print('True')
            else:
                print('False')
            """)

        self.assertCodeExecution("""
            x = 5
            if x <= 5:
                print('True')
            else:
                print('False')
            """)

        self.assertCodeExecution("""
            x = 10
            if x <= 5:
                print('True')
            else:
                print('False')
            """)

    def test_gt(self):
        self.assertCodeExecution("""
            x = 10
            if x > 5:
                print('True')
            else:
                print('False')
            """)

        self.assertCodeExecution("""
            x = 5
            if x > 5:
                print('True')
            else:
                print('False')
            """)

        self.assertCodeExecution("""
            x = 1
            if x > 5:
                print('True')
            else:
                print('False')
            """)

    def test_ge(self):
        self.assertCodeExecution("""
            x = 10
            if x >= 5:
                print('True')
            else:
                print('False')
            """)

        self.assertCodeExecution("""
            x = 5
            if x >= 5:
                print('True')
            else:
                print('False')
            """)

        self.assertCodeExecution("""
            x = 1
            if x >= 5:
                print('True')
            else:
                print('False')
            """)

    def test_eq(self):
        self.assertCodeExecution("""
            x = 10
            if x == 5:
                print('True')
            else:
                print('False')
            """)

        self.assertCodeExecution("""
            x = 5
            if x == 5:
                print('True')
            else:
                print('False')
            """)

    def test_ne(self):
        self.assertCodeExecution("""
            x = 5
            if x != 5:
                print('True')
            else:
                print('False')
            """)

        self.assertCodeExecution("""
            x = 10
            if x != 5:
                print('True')
            else:
                print('False')
            """)
