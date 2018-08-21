from unittest import expectedFailure

from ..utils import TranspileTestCase


class ClosureTests(TranspileTestCase):
    def test_deep_nested(self):
        self.assertCodeExecution("""
            def level3():
                def level2():
                    def level1():
                        print("hello")
                    level1()
                level2()
            level3()
            """, run_in_function=False)

    def test_rebind_closure_var_before_closure_construction(self):
        self.assertCodeExecution("""
            def func():
                closure_var = 'before nested is defined'
                def nested():
                    print(closure_var)
                closure_var = 'after nested is defined'
                nested()
            func()
            """)

    def test_generator_closure(self):
        self.assertCodeExecution("""
            def func():
                closure_var = 'hello world'
                def gen():
                    print(closure_var)
                    yield
                next(gen())
            func()

            def gen():
                closure_var = 'hello world'
                def func():
                    print(closure_var)
                func()
                yield
            next(gen())
            """)

    @expectedFailure
    def test_class_closure(self):
        self.assertCodeExecution("""
            def func():
                closure_var = 'hello world'
                class Inner:
                    print(closure_var)
                Inner()
            func()

            def gen():
                closure_var = 'hello world'
                class Inner:
                    print(closure_var)
                Inner()
                yield
            next(gen())
            """)

    @expectedFailure
    def test_method_closure(self):
        self.assertCodeExecution("""
            def func():
                closure_var = 'hello world'
                class Inner:
                    def method(self):
                        print(closure_var)
                Inner().method()
            func()

            def gen():
                closure_var = 'hello world'
                class Inner:
                    def method(self):
                        print(closure_var)
                Inner().method()
                yield
            next(gen())
            """)
