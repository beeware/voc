def test_function():
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
    try:
        print("obj.attr =", obj.attr)
        print("Shouldn't be able to access attribute.")
    except AttributeError:
        print("Couldn't access attribute.")
    print("Done.")
    
test_function()