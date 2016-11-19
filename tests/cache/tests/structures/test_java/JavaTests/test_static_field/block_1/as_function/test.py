def test_function():
    from com.example import MyClass
    
    print("Class is", MyClass)
    obj1 = MyClass()
    print("Static field is", MyClass.static_field)
    MyClass.static_field = 37
    print("Updated static field is", MyClass.static_field)
    print("Static field from instance is", obj1.static_field)
    MyClass.static_field = 42
    print("Updated static field from instance is", obj1.static_field)
    print("Done.")
    
test_function()