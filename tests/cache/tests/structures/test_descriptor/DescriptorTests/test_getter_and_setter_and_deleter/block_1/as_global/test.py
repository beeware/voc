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
try:
    print("obj.attr =", obj.attr)
    print("Shouldn't be able to access attribute.")
except AttributeError:
    print("Couldn't access attribute.")
print("Done.")
