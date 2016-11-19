def test_function():
    from com.example import MyClass
    
    print("Class is", MyClass)
    obj = MyClass()
    print("Static method is", MyClass.method)
    MyClass.method()
    print("Static method from instance is", obj.method)
    obj.method()
    print("Done.")
    
test_function()