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
