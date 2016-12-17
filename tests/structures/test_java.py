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
            """,
            run_in_function=False)

    def test_most_specific_constructor(self):
        "The most specific constructor for a native Java class will be selected based on argument."
        self.assertJavaExecution(
            """
            from com.example import MyClass

            obj1 = MyClass()
            obj2 = MyClass(1.234)
            obj3 = MyClass(3742)

            print("Done.")
            """,
            java={
                'com/example/MyClass': """
                package com.example;

                public class MyClass {
                    public MyClass() {
                        System.out.println("No argument");
                    }

                    public MyClass(int arg) {
                        System.out.println("Integer argument " + arg);
                    }

                    public MyClass(double arg) {
                        System.out.println("Double argument " + arg);
                    }
                }
                """
            },
            out="""
            No argument
            Double argument 1.234
            Integer argument 3742
            Done.
            """, run_in_function=False)

    def test_field(self):
        "Native fields on an instance can be accessed"
        self.assertJavaExecution(
            """
            from com.example import MyClass

            print("Class is", MyClass)
            obj1 = MyClass()
            print("Field is", MyClass.field)
            print("Field from instance is", obj1.field)
            obj1.field = 37
            print("Updated Field from instance is", obj1.field)
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
                Updated Field from instance is 37
                Done.
                """)

    def test_static_field(self):
        "Class constants can be accessed"
        self.assertJavaExecution(
            """
            from com.example import MyClass

            print("Class is", MyClass)
            obj1 = MyClass()
            print("Static field is", MyClass.static_field)
            MyClass.static_field = 37
            print("Updated static field is", MyClass.static_field)
            print("Static field from instance is", obj1.static_field)
            MyClass.static_field = 42
            print("Updated static field from instance is", obj1.static_field)
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
                Updated static field is 37
                Static field from instance is 37
                Updated static field from instance is 42
                Done.
                """)

    def test_superclass_field(self):
        "Native fields defined on a superclass can be accessed"
        self.assertJavaExecution(
            """
            from com.example import MyBase, MyClass

            print("Base class is", MyBase)
            print("Class is", MyClass)
            obj1 = MyClass()
            print("Base field on superclass is", MyBase.base_field)
            print("Base field is", MyClass.base_field)
            print("Base field from instance is", obj1.base_field)
            print("Field is", MyClass.field)
            print("Field from instance is", obj1.field)
            print("Done.")
            """,
            java={
                'com/example/MyBase': """
                package com.example;

                public class MyBase {
                    public int base_field = 37;
                }
                """,
                'com/example/MyClass': """
                package com.example;

                public class MyClass extends MyBase {
                    public int field = 42;
                }
                """
            },
            out="""
                Base class is <class 'com.example.MyBase'>
                Class is <class 'com.example.MyClass'>
                Base field on superclass is <unbound native field public int com.example.MyBase.base_field>
                Base field is <unbound native field public int com.example.MyBase.base_field>
                Base field from instance is 37
                Field is <unbound native field public int com.example.MyClass.field>
                Field from instance is 42
                Done.
                """)

    def test_superclass_static_field(self):
        "Native static fields defined on a superclass can be accessed"
        self.assertJavaExecution(
            """
            from com.example import MyBase, MyClass

            print("Base class is", MyBase)
            print("Class is", MyClass)
            obj1 = MyClass()
            print("Static base field on superclass is", MyBase.base_static_field)
            print("Static base field is", MyClass.base_static_field)
            print("Static base field from instance is", obj1.base_static_field)
            print("Static field is", MyClass.static_field)
            print("Static field from instance is", obj1.static_field)
            print("Done.")
            """,
            java={
                'com/example/MyBase': """
                package com.example;

                public class MyBase {
                    public static int base_static_field = 37;
                }
                """,
                'com/example/MyClass': """
                package com.example;

                public class MyClass extends MyBase {
                    public static int static_field = 42;
                }
                """
            },
            out="""
                Base class is <class 'com.example.MyBase'>
                Class is <class 'com.example.MyClass'>
                Static base field on superclass is 37
                Static base field is 37
                Static base field from instance is 37
                Static field is 42
                Static field from instance is 42
                Done.
                """)

    def test_constant(self):
        "Instance constants can be accessed"
        self.assertJavaExecution(
            """
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
        self.assertJavaExecution(
            """
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

    def test_method(self):
        "Native methods on an instance can be accessed"
        self.assertJavaExecution(
            """
            from com.example import MyClass

            print("Class is", MyClass)
            obj = MyClass()
            print("Method is", MyClass.method)
            print("Method from instance is", obj.method)
            obj.method()
            print("Done.")
            """,
            java={
                'com/example/MyClass': """
                package com.example;

                public class MyClass {
                    public void method() {
                        System.out.println("Hello from the instance!");
                    }
                }
                """
            },
            out="""
                Class is <class 'com.example.MyClass'>
                Method is <native function com.example.MyClass.method>
                Method from instance is <bound native method com.example.MyClass.method of <Native com.example.MyClass object at 0xXXXXXXXX>>
                Hello from the instance!
                Done.
                """) # noqa

    def test_static_method(self):
        "Native static methods on an instance can be accessed"
        self.assertJavaExecution(
            """
            from com.example import MyClass

            print("Class is", MyClass)
            obj = MyClass()
            print("Static method is", MyClass.method)
            MyClass.method()
            print("Static method from instance is", obj.method)
            obj.method()
            print("Done.")
            """,
            java={
                'com/example/MyClass': """
                package com.example;

                public class MyClass {
                    public static void method() {
                        System.out.println("Hello from the class!");
                    }
                }
                """
            },
            out="""
                Class is <class 'com.example.MyClass'>
                Static method is <native function com.example.MyClass.method>
                Hello from the class!
                Static method from instance is <bound native method com.example.MyClass.method of <Native com.example.MyClass object at 0xXXXXXXXX>>
                Hello from the class!
                Done.
                """) # noqa

    def test_superclass_method(self):
        "Native methods defined on a superclass can be accessed"
        self.assertJavaExecution(
            """
            from com.example import MyBase, MyClass

            print("Base class is", MyBase)
            print("Class is", MyClass)

            print("Base method on superclass is", MyBase.base_method)
            print("Method on superclass is", MyBase.method)

            print("Base method is", MyClass.base_method)
            print("Method is", MyClass.method)

            obj1 = MyBase()
            print("Base method from superclass instance is", obj1.base_method)
            obj1.base_method()
            print("Method from superclass instance is", obj1.method)
            obj1.method()

            obj2 = MyClass()
            print("Base method from instance is", obj2.base_method)
            obj2.base_method()
            print("Method from instance is", obj2.method)
            obj2.method()
            print("Done.")
            """,
            java={
                'com/example/MyBase': """
                package com.example;

                public class MyBase {
                    public void base_method() {
                        System.out.println("Hello from the base!");
                    }

                    public void method() {
                        System.out.println("Goodbye from the base!");
                    }
                }
                """,
                'com/example/MyClass': """
                package com.example;

                public class MyClass extends MyBase {
                    public void method() {
                        System.out.println("Hello from the instance!");
                    }
                }
                """
            },
            out="""
                Base class is <class 'com.example.MyBase'>
                Class is <class 'com.example.MyClass'>
                Base method on superclass is <native function com.example.MyBase.base_method>
                Method on superclass is <native function com.example.MyBase.method>
                Base method is <native function com.example.MyBase.base_method>
                Method is <native function com.example.MyClass.method>
                Base method from superclass instance is <bound native method com.example.MyBase.base_method of <Native com.example.MyBase object at 0xXXXXXXXX>>
                Hello from the base!
                Method from superclass instance is <bound native method com.example.MyBase.method of <Native com.example.MyBase object at 0xXXXXXXXX>>
                Goodbye from the base!
                Base method from instance is <bound native method com.example.MyBase.base_method of <Native com.example.MyClass object at 0xXXXXXXXX>>
                Hello from the base!
                Method from instance is <bound native method com.example.MyClass.method of <Native com.example.MyClass object at 0xXXXXXXXX>>
                Hello from the instance!
                Done.
                """) # noqa

    def test_superclass_static_method(self):
        "Native static methods defined on a superclass can be accessed"
        self.assertJavaExecution(
            """
            from com.example import MyBase, MyClass

            print("Base class is", MyBase)
            print("Class is", MyClass)

            print("Static base method on superclass is", MyBase.base_static_method)
            MyBase.base_static_method()
            print("Static method on superclass is", MyBase.static_method)
            MyBase.static_method()

            print("Static base method is", MyClass.base_static_method)
            MyClass.base_static_method()
            print("Static method is", MyClass.static_method)
            MyClass.static_method()

            obj1 = MyBase()
            print("Base static method from superclass instance is", obj1.base_static_method)
            obj1.base_static_method()
            print("Static method from superclass instance is", obj1.static_method)
            obj1.static_method()

            obj2 = MyClass()
            print("Base static method from instance is", obj2.base_static_method)
            obj2.base_static_method()
            print("Static method from instance is", obj2.static_method)
            obj2.static_method()
            print("Done.")
            """,
            java={
                'com/example/MyBase': """
                package com.example;

                public class MyBase {
                    public static void base_static_method() {
                        System.out.println("Hello from the base!");
                    }

                    public static void static_method() {
                        System.out.println("Goodbye from the base!");
                    }
                }
                """,
                'com/example/MyClass': """
                package com.example;

                public class MyClass extends MyBase {
                    public static void static_method() {
                        System.out.println("Hello from the class!");
                    }
                }
                """
            },
            out="""
                Base class is <class 'com.example.MyBase'>
                Class is <class 'com.example.MyClass'>
                Static base method on superclass is <native function com.example.MyBase.base_static_method>
                Hello from the base!
                Static method on superclass is <native function com.example.MyBase.static_method>
                Goodbye from the base!
                Static base method is <native function com.example.MyBase.base_static_method>
                Hello from the base!
                Static method is <native function com.example.MyClass.static_method>
                Hello from the class!
                Base static method from superclass instance is <bound native method com.example.MyBase.base_static_method of <Native com.example.MyBase object at 0xXXXXXXXX>>
                Hello from the base!
                Static method from superclass instance is <bound native method com.example.MyBase.static_method of <Native com.example.MyBase object at 0xXXXXXXXX>>
                Goodbye from the base!
                Base static method from instance is <bound native method com.example.MyBase.base_static_method of <Native com.example.MyClass object at 0xXXXXXXXX>>
                Hello from the base!
                Static method from instance is <bound native method com.example.MyClass.static_method of <Native com.example.MyClass object at 0xXXXXXXXX>>
                Hello from the class!
                Done.
                """)  # noqa

    def test_inner_class_constant(self):
        "Constants on an inner class can be accessed"
        self.assertJavaExecution(
            """
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

    def test_inner_class_method(self):
        "Inner classes can be instantiated, and methods invoked"
        self.assertJavaExecution(
            """
            from com.example import OuterClass

            print("Outer class is", OuterClass)
            obj1 = OuterClass()
            obj1.method()

            print("Inner class is", OuterClass.InnerClass)
            obj2 = OuterClass.InnerClass(obj1)
            obj2.method()

            print("Done.")
            """,
            java={
                'com/example/OuterClass': """
                package com.example;

                public class OuterClass {
                    public class InnerClass {
                        public void method() {
                            System.out.println("Hello from the inside!");
                        }
                    }

                    public void method() {
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
        self.assertJavaExecution(
            """
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

    def test_static_inner_class_method(self):
        "Static inner classes can be instantiated, and methods invoked"
        self.assertJavaExecution(
            """
            from com.example import OuterClass

            print("Outer class is", OuterClass)
            obj1 = OuterClass()
            obj1.method()

            print("Inner class is", OuterClass.InnerClass)
            obj2 = OuterClass.InnerClass()
            obj2.method()

            print("Done.")
            """,
            java={
                'com/example/OuterClass': """
                package com.example;

                public class OuterClass {
                    public static class InnerClass {
                        public void method() {
                            System.out.println("Hello from the inside!");
                        }
                    }

                    public void method() {
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

    def test_primitive_conversion(self):
        "Primitive types are converted correctly"
        self.assertJavaExecution(
            """
            from com.example import MyObject

            obj = MyObject()

            result = obj.method(3)
            print('Result is', result)

            result = obj.method(3.14159)
            print('Result is', result)

            result = obj.method(True)
            print('Result is', result)

            print("Done.")
            """,
            java={
                'com/example/MyObject': """
                package com.example;

                public class MyObject {
                    public int method(int x) {
                        System.out.println("Hello from int method: " + x);
                        return x * 2;
                    }

                    public float method(float x) {
                        System.out.println("Hello from float method: " + x);
                        return x * 2.5f;
                    }

                    public boolean method(boolean x) {
                        System.out.println("Hello from boolean method: " + x);
                        return !x;
                    }
                }
                """
            },
            out="""
                Hello from int method: 3
                Result is 6
                Hello from float method: 3.14159
                Result is 7.853975296020508
                Hello from boolean method: true
                Result is False
                Done.
                """)

    def test_primitive_zero_conversion(self):
        "Primitive representations of 'false' values are converted correctly"
        self.assertJavaExecution(
            """
            from com.example import MyObject

            obj = MyObject()

            result = obj.method(0)
            print('Result is', result)

            result = obj.method(0.0)
            print('Result is', result)

            result = obj.method(False)
            print('Result is', result)

            print("Done.")
            """,
            java={
                'com/example/MyObject': """
                package com.example;

                public class MyObject {
                    public int method(int x) {
                        System.out.println("Hello from int method: " + x);
                        return x * 2;
                    }

                    public float method(float x) {
                        System.out.println("Hello from float method: " + x);
                        return x * 2.5f;
                    }

                    public boolean method(boolean x) {
                        System.out.println("Hello from boolean method: " + x);
                        return !x;
                    }
                }
                """
            },
            out="""
                Hello from int method: 0
                Result is 0
                Hello from float method: 0.0
                Result is 0.0
                Hello from boolean method: false
                Result is True
                Done.
                """)

    def test_attribute_on_reference(self):
        self.assertJavaExecution(
            """
            from com.example import BaseObject, Controller

            class TestObject(extends=com.example.BaseObject):
                def __init__(self, v1, v2):
                    # super().__init__(v1)
                    self.extra1 = v2

                def process(self) -> None:
                    print("Processed Base data is %s" % self.base)
                    print("Processed Extra data 1 is %s" % self.extra1)
                    print("Processed Extra data 2 is %s" % self.extra2)

            obj = TestObject(37, 99)
            obj.extra2 = 42

            print("Base data is %s" % obj.base)
            print("Extra data 1 is %s" % obj.extra1)
            print("Extra data 2 is %s" % obj.extra2)

            controller = Controller()

            controller.setObject(obj)

            controller.poke()

            print("Done.")
            """,
            java={
                'com/example/ObjIFace': """
                package com.example;

                public interface ObjIFace {
                    public void process();
                }

                """,
                'com/example/Controller': """
                package com.example;

                public class Controller {
                    public ObjIFace obj;

                    public Controller() {
                    }

                    public void setObject(ObjIFace o) {
                        this.obj = o;
                    }

                    public void poke() {
                        this.obj.process();
                    }
                }

                """,
                'com/example/BaseObject': """
                package com.example;

                public class BaseObject implements com.example.ObjIFace {
                    public int base;

                    public BaseObject() {
                        base = 1;
                    }

                    public BaseObject(int v) {
                        base = v;
                    }

                    public void process() {
                        System.out.println("Do nothing...");
                    }
                }
                """
            },
            out="""
                Base data is 1
                Extra data 1 is 99
                Extra data 2 is 42
                Processed Base data is 1
                Processed Extra data 1 is 99
                Processed Extra data 2 is 42
                Done.
                """,
            run_in_function=False)
