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

    def test_degrees(self):
    	self.assertCodeExecution("""
    		import math
    		print(math.degrees(1))
    		""")

    def test_radians(self):
    	self.assertCodeExecution("""
    		import math
    		print(math.radians(180))
    		""")

    @expectedFailure
    def test_hypot(self):
    	self.assertCodeExecution("""
    		import math
    		print(math.hypot(3,4))
    		""")
    