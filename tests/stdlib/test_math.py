from unittest import expectedFailure

from ..utils import TranspileTestCase

class MathModuleTests(TranspileTestCase):
    # Trigonometric functions
    def test_sin(self):
        self.assertCodeExecution("""
            import math
            print(math.sin(1))
            """)

    def test_cos(self):
        self.assertCodeExecution("""
            import math
            print(math.cos(1))
            """)

    def test_tan(self):
        self.assertCodeExecution("""
            import math
            print(math.tan(1))
            """)
