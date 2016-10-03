from ..utils import TranspileTestCase


class DescriptorTests(TranspileTestCase):
    def test_getter(self):
        self.assertCodeExecution("""
            class MyObject:
                def getter(self):
                    print("Got attribute")
                    return 1234

                attr = property(getter)

            obj = MyObject()
            print("obj.attr =", obj.attr)

            try:
                obj.attr = 2345
                print("Shouldn't be able to set attribute.")
            except AttributeError:
                print("Couldn't set attribute.")

            try:
                del obj.attr
                print("Shouldn't be able to delete attribute.")
            except AttributeError:
                print("Couldn't delete attribute.")

            print("Done.")
            """)

    def test_getter_and_setter(self):
        self.assertCodeExecution("""
            class MyObject:
                def __init__(self):
                    self._attr = None

                def getter(self):
                    print("Got attribute")
                    return self._attr

                def setter(self, value):
                    print("Setting attribute")
                    self._attr = value * 2
                    print("Attribute set")

                attr = property(getter, setter)

            obj = MyObject()
            print("obj.attr =", obj.attr)
            obj.attr = 2345
            print("obj.attr =", obj.attr)

            try:
                del obj.attr
                print("Shouldn't be able to delete attribute.")
            except AttributeError:
                print("Couldn't delete attribute.")

            print("Done.")
            """)

    def test_getter_and_setter_and_deleter(self):
        self.assertCodeExecution("""
            class MyObject:
                def __init__(self):
                    self._attr = None

                def getter(self):
                    print("Got attribute")
                    return self._attr

                def setter(self, value):
                    print("Setting attribute")
                    self._attr = value * 2
                    print("Attribute set")

                def deleter(self):
                    print("Deleting attribute")
                    self._attr = 42
                    print("Attribute deleted")

                attr = property(getter, setter, deleter)

            obj = MyObject()
            print("obj.attr =", obj.attr)
            obj.attr = 2345
            print("obj.attr =", obj.attr)
            del obj.attr
            print("obj.attr =", obj.attr)
            print("Done.")
            """)

    def test_with_decorators(self):
        self.assertCodeExecution("""
            class MyObject:
                def __init__(self):
                    self._attr = None

                @property
                def attr(self):
                    print("Got attribute")
                    return self._attr

                @attr.setter
                def attr(self, value):
                    print("Setting attribute")
                    self._attr = value * 2
                    print("Attribute set")

                @attr.deleter
                def attr(self):
                    print("Deleting attribute")
                    self._attr = 42
                    print("Attribute deleted")

            obj = MyObject()
            print("obj.attr =", obj.attr)
            obj.attr = 2345
            print("obj.attr =", obj.attr)
            del obj.attr
            print("obj.attr =", obj.attr)
            print("Done.")
            """)

    def test_with_decorators_misnamed_methods(self):
        self.assertCodeExecution("""
            class MyObject:
                def __init__(self):
                    self._attr = None

                @property
                def attr(self):
                    print("Got attribute")
                    return self._attr

                @attr.setter
                def attr1(self, value):
                    print("Setting attribute")
                    self._attr = value * 2
                    print("Attribute set")

                @attr.deleter
                def attr2(self):
                    print("Deleting attribute")
                    self._attr = 42
                    print("Attribute deleted")

            obj = MyObject()
            print("obj.attr =", obj.attr)
            print("obj.attr1 =", obj.attr1)
            print("obj.attr2 =", obj.attr2)
            obj.attr1 = 2345
            print("obj.attr =", obj.attr)
            print("obj.attr1 =", obj.attr1)
            print("obj.attr2 =", obj.attr2)
            try:
                obj.attr2 = 3456
                print("Shouldn't be able to set value of attr2")
            except AttributeError:
                print("Can't set value of attr2")
            del obj.attr2
            print("obj.attr =", obj.attr)
            print("obj.attr1 =", obj.attr1)
            print("obj.attr2 =", obj.attr2)
            print("Done.")
            """)
