from unittest import expectedFailure

from ..utils import TranspileTestCase


class JavaTests(TranspileTestCase):

    def test_multiple_constructors(self):
        "The appropriate constructor for a native Java class can be interpolated from args"
        self.assertJavaExecution(
            """
            from java.lang import StringBuilder

            builder = StringBuilder("Hello, ")

            builder.append("world")

            print(builder)
            print("Done.")
            """,
            """
            Hello, world
            Done.
            """, run_in_function=False)

    def test_field(self):
        "Native fields on an instance can be accessed"
        self.assertJavaExecution("""
                from com.example import MyClass

                print("Class is", MyClass)
                obj1 = MyClass()
                print("Field is", MyClass.field)
                print("Field from instance is", obj1.field)
                print("Done.")
                """,
            java={
                'com/example/MyClass': """
                package com.example;

                public class MyClass {
                    public int field = 42;
                }
                """
            },
            out="""
                Class is <class 'com.example.MyClass'>
                Field is <unbound native field public int com.example.MyClass.field>
                Field from instance is 42
                Done.
                """)

    def test_static_field(self):
        "Class constants can be accessed"
        self.assertJavaExecution("""
                from com.example import MyClass

                print("Class is", MyClass)
                obj1 = MyClass()
                print("Static field is", MyClass.static_field)
                print("Static field from instance is", obj1.static_field)
                print("Done.")
                """,
            java={
                'com/example/MyClass': """
                package com.example;

                public class MyClass {
                    public static int static_field = 42;
                }
                """
            },
            out="""
                Class is <class 'com.example.MyClass'>
                Static field is 42
                Static field from instance is 42
                Done.
                """)

    def test_constant(self):
        "Instance constants can be accessed"
        self.assertJavaExecution("""
                from com.example import MyClass

                print("Class is", MyClass)
                obj1 = MyClass()
                print("Constant is", MyClass.CONSTANT)
                print("Constant from instance is", obj1.CONSTANT)
                print("Done.")
                """,
            java={
                'com/example/MyClass': """
                package com.example;

                public class MyClass {
                    public final int CONSTANT = 42;
                }
                """
            },
            out="""
                Class is <class 'com.example.MyClass'>
                Constant is <unbound native field public final int com.example.MyClass.CONSTANT>
                Constant from instance is 42
                Done.
                """)

    def test_static_constant(self):
        "Class constants can be accessed"
        self.assertJavaExecution("""
                from com.example import MyClass

                print("Class is", MyClass)
                obj1 = MyClass()
                print("Static constant is", MyClass.STATIC_CONSTANT)
                print("Static constant from instance is", obj1.STATIC_CONSTANT)
                print("Done.")
                """,
            java={
                'com/example/MyClass': """
                package com.example;

                public class MyClass {
                    public static final int STATIC_CONSTANT = 42;
                }
                """
            },
            out="""
                Class is <class 'com.example.MyClass'>
                Static constant is 42
                Static constant from instance is 42
                Done.
                """)

    def test_inner_class_constant(self):
        "Constants on an inner class can be accessed"
        self.assertJavaExecution("""
                from com.example import OuterClass

                print("Outer class is", OuterClass)
                print("Outer constant is", OuterClass.OUTER_CONSTANT)

                print("Inner class is", OuterClass.InnerClass)
                print("Inner constant is", OuterClass.InnerClass.INNER_CONSTANT)

                print("Done.")
                """,
            java={
                'com/example/OuterClass': """
                package com.example;

                public class OuterClass {
                    public static final int OUTER_CONSTANT = 42;

                    public static class InnerClass {
                        public static final int INNER_CONSTANT = 37;
                    }
                }
                """
            },
            out="""
                Outer class is <class 'com.example.OuterClass'>
                Outer constant is 42
                Inner class is <class 'com.example.OuterClass$InnerClass'>
                Inner constant is 37
                Done.
                """)

    @expectedFailure
    def test_inner_class_methods(self):
        "Inner classes can be instantiated, and methods invoked"
        self.assertJavaExecution("""
                from com.example import OuterClass

                print("Outer class is", OuterClass)
                obj1 = OuterClass()
                obj1.doStuff()

                print("Inner class is", OuterClass.InnerClass)
                obj2 = OuterClass.InnerClass()
                obj2.doStuff()

                print("Done.")
                """,
            java={
                'com/example/OuterClass': """
                package com.example;

                public class OuterClass {
                    public class InnerClass {
                        public void doStuff() {
                            System.out.println("Hello from the inside!");
                        }
                    }

                    public void doStuff() {
                        System.out.println("Hello from the outside!");
                    }
                }
                """
            },
            out="""
                Outer class is <class 'com.example.OuterClass'>
                Hello from the outside!
                Inner class is <class 'com.example.OuterClass$InnerClass'>
                Hello from the inside!
                Done.
                """)


    def test_static_inner_class_constant(self):
        "Constants on a static inner class can be accessed"
        self.assertJavaExecution("""
                from com.example import OuterClass

                print("Outer class is", OuterClass)
                print("Outer constant is", OuterClass.OUTER_CONSTANT)

                print("Inner class is", OuterClass.InnerClass)
                print("Inner constant is", OuterClass.InnerClass.INNER_CONSTANT)

                print("Done.")
                """,
            java={
                'com/example/OuterClass': """
                package com.example;

                public class OuterClass {
                    public static final int OUTER_CONSTANT = 42;

                    public static class InnerClass {
                        public static final int INNER_CONSTANT = 37;
                    }
                }
                """
            },
            out="""
                Outer class is <class 'com.example.OuterClass'>
                Outer constant is 42
                Inner class is <class 'com.example.OuterClass$InnerClass'>
                Inner constant is 37
                Done.
                """)

    def test_static_inner_class_methods(self):
        "Static inner classes can be instantiated, and methods invoked"
        self.assertJavaExecution("""
                from com.example import OuterClass

                print("Outer class is", OuterClass)
                obj1 = OuterClass()
                obj1.doStuff()

                print("Inner class is", OuterClass.InnerClass)
                obj2 = OuterClass.InnerClass()
                obj2.doStuff()

                print("Done.")
                """,
            java={
                'com/example/OuterClass': """
                package com.example;

                public class OuterClass {
                    public static class InnerClass {
                        public void doStuff() {
                            System.out.println("Hello from the inside!");
                        }
                    }

                    public void doStuff() {
                        System.out.println("Hello from the outside!");
                    }
                }
                """
            },
            out="""
                Outer class is <class 'com.example.OuterClass'>
                Hello from the outside!
                Inner class is <class 'com.example.OuterClass$InnerClass'>
                Hello from the inside!
                Done.
                """)
