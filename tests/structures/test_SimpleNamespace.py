from ..utils import TranspileTestCase


class SimpleNamespaceTests(TranspileTestCase):
    def test_creation(self):
        self.assertCodeExecution("""
            import types

            s = types.SimpleNamespace(a=1, b=2)
            print(s)
            print(s.a)
            print(s.b)

            try:
                s = types.SimpleNamespace(1, b=2)
                print("should not print this")
            except TypeError as e:
                print(e)
            """)

    def test_eq(self):
        self.assertCodeExecution("""
            import types

            s1 = types.SimpleNamespace(a=1, b=2)
            s2 = types.SimpleNamespace(b=2, a=1)
            print(s1 == s2)

            s3 = types.SimpleNamespace(b=2, a=1, c=3)
            print(s1 == s3)
            """)
