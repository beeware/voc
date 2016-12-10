def test_function():
    from com.example import OuterClass
    
    print("Outer class is", OuterClass)
    obj1 = OuterClass()
    obj1.method()
    
    print("Inner class is", OuterClass.InnerClass)
    obj2 = OuterClass.InnerClass(obj1)
    obj2.method()
    
    print("Done.")
    
test_function()