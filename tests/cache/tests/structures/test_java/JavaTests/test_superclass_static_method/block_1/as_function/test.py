def test_function():
    from com.example import MyBase, MyClass
    
    print("Base class is", MyBase)
    print("Class is", MyClass)
    
    print("Static base method on superclass is", MyBase.base_static_method)
    MyBase.base_static_method()
    print("Static method on superclass is", MyBase.static_method)
    MyBase.static_method()
    
    print("Static base method is", MyClass.base_static_method)
    MyClass.base_static_method()
    print("Static method is", MyClass.static_method)
    MyClass.static_method()
    
    obj1 = MyBase()
    print("Base static method from superclass instance is", obj1.base_static_method)
    obj1.base_static_method()
    print("Static method from superclass instance is", obj1.static_method)
    obj1.static_method()
    
    obj2 = MyClass()
    print("Base static method from instance is", obj2.base_static_method)
    obj2.base_static_method()
    print("Static method from instance is", obj2.static_method)
    obj2.static_method()
    print("Done.")
    
test_function()