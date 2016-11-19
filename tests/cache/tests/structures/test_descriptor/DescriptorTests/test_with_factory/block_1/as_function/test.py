def test_function():
    def make_attr(name, multiplier):
        def getter(self):
            return getattr(self, '_' + name)
    
        def setter(self, value):
            setattr(self, '_' + name, value * multiplier)
    
        def deleter(self):
            delattr(self, '_' + name)
    
        return property(getter, setter, deleter)
    
    class MyObject:
        doubled = make_attr('doubled', 2)
    
    MyObject.tripled = make_attr('tripled', 3)
    
    obj = MyObject()
    obj._doubled = 10
    obj._tripled = 20
    
    print(obj.doubled)
    print(obj.tripled)
    obj.doubled = 1234
    obj.tripled = 1234
    print(obj.doubled)
    print(obj.tripled)
    del obj.doubled
    del obj.tripled
    try:
        print("obj.doubled =", obj.doubled)
        print("Shouldn't be able to access attribute.")
    except AttributeError:
        print("Couldn't access attribute.")
    try:
        print("obj.tripled =", obj.tripled)
        print("Shouldn't be able to access attribute.")
    except AttributeError:
        print("Couldn't access attribute.")
    
test_function()