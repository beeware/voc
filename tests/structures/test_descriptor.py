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

                def deleter(self, value):
                    print("Setting attribute")
                    self._attr = value * 2
                    print("Attribute set")

                attr = property(getter)

            obj = MyObject()
            print("obj.attr =", obj.attr)
            obj.attr = 2345
            print("obj.attr =", obj.attr)
            del obj.attr
            print("obj.attr =", obj.attr)
            print("Done.")
            """)