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

    @expectedFailure
    def test_ceil(self): 
        self.assertCodeExecution("""
            import math
            print(math.ceil(1.2))
        """)

    @expectedFailure
    def test_floor(self): 
        self.assertCodeExecution("""
            import math
            print(math.floor(1.2))
        """)

    @expectedFailure
    def test_sqrt(self): 
        self.assertCodeExecution("""
            import math
            print(math.sqrt(4))
        """)
        self.assertCodeExecution("""
            import math
            print(math.sqrt(1.44))
        """)