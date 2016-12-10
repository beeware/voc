def test_function():
    from com.example import MyBase, MyClass
    
    print("Base class is", MyBase)
    print("Class is", MyClass)
    obj1 = MyClass()
    print("Static base field on superclass is", MyBase.base_static_field)
    print("Static base field is", MyClass.base_static_field)
    print("Static base field from instance is", obj1.base_static_field)
    print("Static field is", MyClass.static_field)
    print("Static field from instance is", obj1.static_field)
    print("Done.")
    
test_function()