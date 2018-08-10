from unittest import expectedFailure

from .. utils import TranspileTestCase


class ObjectTests(TranspileTestCase):
    @expectedFailure
    def test_setitem(self):
        self.assertCodeExecution("""
            class MyClass:
                def __setitem__(self, key, item):
                    print("In __setitem__")

            obj = MyClass()
            obj[0] = 0
            """)

    def test_getitem(self):
        self.assertCodeExecution("""
            class MyClass:
                def __getitem__(self, key):
                    print("In __getitem__")

            obj = MyClass()
            print(obj[0])
            """)

    @expectedFailure
    def test_getattribute(self):
        self.assertCodeExecution("""
            class MyClass:
                pass

            obj = MyClass()
            try:
                print(obj.a)
            except AttributeError as e:
                print(e)

            class MyClass1:
                def __getattribute__(self, name):
                    return name

            obj = MyClass1()
            print(obj.a)
        """)

    @expectedFailure
    def test_getattr(self):
        self.assertCodeExecution("""
            class MyClass:
                pass

            obj = MyClass()
            try:
                print(obj.a)
            except AttributeError as e:
                print(e)

            class MyClass1:
                def __getattr__(self, name):
                    return name

            obj = MyClass1()
            print(obj.a)
        """)

    @expectedFailure
    def test_hash(self):
        self.assertCodeExecution("""
            class MyClass:
                pass

            obj = MyClass()
            hash_code = obj.hash()
            print(isinstance(hash_code, int))
        """)

    @expectedFailure
    def test_repr(self):
        self.assertCodeExecution("""
            class MyClass:
                pass

            obj = MyClass()
            print(obj.repr())

            class MyClass1:
                def __repr__(self):
                    return "I am a MyClass1!"

            obj = MyClass1()
            print(obj.repr())
        """)

    def test_bytes(self):
        self.assertCodeExecution("""
            class MyClass:
                pass

            obj = MyClass()
            try:
                print(bytes(obj))
            except TypeError as e:
                print(e)
        """)

    def test_eq(self):
        self.assertCodeExecution("""
            class MyClass:
                pass

            obj1 = MyClass()
            obj2 = MyClass()
            print(obj1 == obj2)
            print(obj1 is obj2)

            class MyClass1:
                def __eq__(self, other):
                    return True

            obj1 = MyClass1()
            obj2 = MyClass1()
            print(obj1 == obj2)
            print(obj1 is obj2)
        """)

    def test_le(self):
        self.assertCodeExecution("""
            class MyClass:
                pass

            obj1 = MyClass()
            obj2 = MyClass()
            try:
                print(obj1 <= obj2)
            except TypeError as e:
                print(e)

            class MyClass1:
                def __le__(self, other):
                    return True

            obj1 = MyClass1()
            obj2 = MyClass1()
            print(obj1 <= obj2)
        """)

    def test_lt(self):
        self.assertCodeExecution("""
            class MyClass:
                pass

            obj1 = MyClass()
            obj2 = MyClass()
            try:
                print(obj1 < obj2)
            except TypeError as e:
                print(e)

            class MyClass1:
                def __lt__(self, other):
                    return True

            obj1 = MyClass1()
            obj2 = MyClass1()
            print(obj1 < obj2)
        """)

    def test_ge(self):
        self.assertCodeExecution("""
            class MyClass:
                pass

            obj1 = MyClass()
            obj2 = MyClass()
            try:
                print(obj1 >= obj2)
            except TypeError as e:
                print(e)

            class MyClass1:
                def __ge__(self, other):
                    return True

            obj1 = MyClass1()
            obj2 = MyClass1()
            print(obj1 >= obj2)
        """)

    def test_gt(self):
        self.assertCodeExecution("""
            class MyClass:
                pass

            obj1 = MyClass()
            obj2 = MyClass()
            try:
                print(obj1 > obj2)
            except TypeError as e:
                print(e)

            class MyClass1:
                def __gt__(self, other):
                    return True

            obj1 = MyClass1()
            obj2 = MyClass1()
            print(obj1 > obj2)
        """)
