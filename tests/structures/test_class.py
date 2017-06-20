from unittest import expectedFailure

from ..utils import TranspileTestCase


class ClassTests(TranspileTestCase):
    def test_minimal(self):
        self.assertCodeExecution("""
            class MyClass:
                pass

            obj = MyClass()
            """, run_in_function=False)

    def test_simple(self):
        self.assertCodeExecution("""
            class MyClass:
                def __init__(self, val):
                    print("VAL: ", val)
                    self.value = val

                def stuff(self, delta):
                    print("DELTA: ", delta)
                    return self.value + delta

            obj = MyClass(4)
            obj.stuff(5)
            """, run_in_function=False)

    def test_subclass_object(self):
        self.assertCodeExecution("""
            class MyClass(object):
                def __init__(self, val):
                    print("VAL: ", val)
                    self.value = val

                def stuff(self, delta):
                    print("DELTA: ", delta)
                    return self.value + delta

            obj = MyClass(4)
            obj.stuff(5)
            """, run_in_function=False)

    def test_method_override(self):
        self.assertCodeExecution("""
            class MyObject:
                def __init__(self, x):
                    self.x = x

                def __str__(self):
                    return "Myobject instance %s" % self.x

            obj = MyObject(37)

            print(obj)
            """, run_in_function=False)

    def test_subclass(self):
        self.assertCodeExecution("""
            class MyBase:
                def __init__(self, x):
                    self.x = x

                def __str__(self):
                    return "Mybase instance %s" % self.x

                def first(self):
                    return self.x * 2


            class MyObject(MyBase):
                def __init__(self, x, y):
                    super().__init__(x)
                    self.y = y

                def __str__(self):
                    return "Myobject instance %s, %s" % (self.x, self.y)

                def second(self):
                    return self.x * self.y

            obj = MyObject(37, 42)

            print(obj)
            print(obj.x)
            print(obj.first())
            print(obj.y)
            print(obj.second())
            """)

    def test_subclass_2_clause_super(self):
        self.assertCodeExecution("""
            class MyBase:
                def __init__(self, x):
                    self.x = x

                def __str__(self):
                    return "Mybase instance %s" % self.x

                def first(self):
                    return self.x * 2


            class MyObject(MyBase):
                def __init__(self, x, y):
                    super(MyObject, self).__init__(x)
                    self.y = y

                def __str__(self):
                    return "Myobject instance %s, %s" % (self.x, self.y)

                def second(self):
                    return self.x * self.y

            obj = MyObject(37, 42)

            print(obj)
            print(obj.x)
            print(obj.first())
            print(obj.y)
            print(obj.second())
            """)

    def test_redefine(self):
        self.assertCodeExecution("""
            class MyClass:
                def __init__(self, val):
                    print("VAL: ", val)
                    self.value = val

                def stuff(self, delta):
                    print("DELTA: ", delta)
                    return self.value + delta

                def stuff(self, delta):
                    print("Redefined DELTA: ", delta)
                    return self.value + delta * 2

            obj = MyClass(4)
            obj.stuff(5)
            """, run_in_function=False)

    def test_overwrite_class_attributes(self):
        self.assertCodeExecution("""
            class MyClass:
                x = 1

            print(MyClass.x)

            inst = MyClass()
            print(inst.x)

            inst.x = 123
            print(inst.x)

            print(MyClass.x)

            inst2 = MyClass()
            inst2.x = 5
            print(inst2.x)
            """, run_in_function=False)


class ClassMethodTests(TranspileTestCase):
    @expectedFailure
    def test_classmethod(self):
        self.assertCodeExecution("""
            class MyClass:
                @classmethod
                def foo(cls, arg1, arg2):
                    print("This is a classmethod on ", cls, arg1, arg2)

            obj = MyClass()
            obj.foo(1, 2)
            MyClass.foo(3, 4)
            """, run_in_function=False)


class StaticMethodTests(TranspileTestCase):
    @expectedFailure
    def test_staticmethod(self):
        self.assertCodeExecution("""
            class MyClass:
                @staticmethod
                def foo(arg1, arg2):
                    print("This is a staticmethod ", arg1, arg2)

            obj = MyClass()
            obj.foo(1, 2)
            MyClass.foo(3, 4)
            """, run_in_function=False)


class InnerClassTests(TranspileTestCase):
    def test_inner_simple(self):
        self.assertCodeExecution("""
            class MyClass:
                class InnerClass:
                    def __init__(self, val):
                        print("VAL: ", val)
                        self.value = val

                    def stuff(self, delta):
                        print("DELTA: ", delta)
                        return self.value + delta

            obj = MyClass.InnerClass(4)
            obj.stuff(5)
        """, run_in_function=False)

    def test_inner_namespaced(self):
        self.assertCodeExecution("""
            class MyClass1:
                class InnerClass:
                    def stuff(self):
                        print('STUFF FROM 1')

            class MyClass2:
                class InnerClass:
                    def stuff(self):
                        print('STUFF FROM 2')

            obj = MyClass1.InnerClass()
            obj.stuff()
            obj = MyClass2.InnerClass()
            obj.stuff()
        """, run_in_function=False)
