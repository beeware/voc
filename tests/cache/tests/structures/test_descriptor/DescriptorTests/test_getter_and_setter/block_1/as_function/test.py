def test_function():
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
    
test_function()