from unittest import expectedFailure

from ..utils import TranspileTestCase

class NonlocalTests(TranspileTestCase):
    def test_nonlocal_func(self):
        self.assertCodeExecution("""
            def func():
                a = 'a from outer'
                b = 'b from outer'
                def nested_func():
                    nonlocal a
                    print(a)
                    a = 'a from inner'
                    print(a)
                    b = 'b from inner'
                    print(b)

                nested_func()
                print(a)
                print(b)
                
            func()
        """)

    @expectedFailure
    def test_nonlocal_class(self):
        self.assertCodeExecution("""
            def func():
                a = 'a from outer'
                b = 'b from outer'
                class Inner():
                    nonlocal a
                    print(a)
                    a = 'a from inner'
                    print(a)
                Inner()
                print(a)
                print(b)
                
            func()
        """)
