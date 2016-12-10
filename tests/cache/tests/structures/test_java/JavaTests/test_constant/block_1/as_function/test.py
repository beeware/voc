def test_function():
    from com.example import MyClass
    
    print("Class is", MyClass)
    obj1 = MyClass()
    print("Constant is", MyClass.CONSTANT)
    print("Constant from instance is", obj1.CONSTANT)
    print("Done.")
    
test_function()