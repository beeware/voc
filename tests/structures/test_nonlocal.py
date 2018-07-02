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

            def func2():
                a = 'a from outer'
                b = 'b from outer'
                def nested_func2():
                    nonlocal a
                    print(a)
                    a = 'a from inner'
                    print(a)
                    def nested_nested_func():
                        nonlocal b
                        print(b)
                        b = 'b from innest'
                        print(b)

                    nested_nested_func()

                nested_func2()
                print(a)
                print(b)

            func2()
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
