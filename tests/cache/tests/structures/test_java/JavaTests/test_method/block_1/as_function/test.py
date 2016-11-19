def test_function():
    from com.example import MyClass
    
    print("Class is", MyClass)
    obj = MyClass()
    print("Method is", MyClass.method)
    print("Method from instance is", obj.method)
    obj.method()
    print("Done.")
    
test_function()