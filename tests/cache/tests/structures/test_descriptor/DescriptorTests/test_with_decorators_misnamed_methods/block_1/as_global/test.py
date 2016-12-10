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
try:
    print("obj.attr2 =", obj.attr2)
    print("Shouldn't be able to access attribute.")
except AttributeError:
    print("Couldn't access attribute.")

print("Done.")
