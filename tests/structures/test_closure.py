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
