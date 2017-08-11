from .utils import TranspileTestCase


class InteroperabilityTest(TranspileTestCase):
    def test_extend_java_class_with_simple_constructor(self):
        self.assertJavaExecution(
            """
            class MyPythonClass(extends=com.example.MyClass):
                pass

            MyPythonClass()
            print("Done.")
            """,
            java={
                'com/example/MyClass': """
                package com.example;

                public class MyClass {
                    public MyClass() {
                        System.out.println("MyClass started");
                    }
                }
                """
            },
            out="""
            MyClass started
            Done.
            """,
        )

    def test_extend_java_class_with_constructor_that_needs_args(self):
        self.assertJavaExecution(
            """
            class MyPythonClass(extends=com.example.MyClass):
                def __init__(self, x: java.lang.Integer) -> void:
                    print('x', x)

            MyPythonClass()
            print("Done.")
            """,
            java={
                'com/example/MyClass': """
                package com.example;

                public class MyClass {
                    public MyClass(Integer x) {
                        System.out.println("MyClass started with " + x);
                    }
                }
                """
            },
            out="""
            MyClass started with 1
            x 1
            Done.
            """,
        )
