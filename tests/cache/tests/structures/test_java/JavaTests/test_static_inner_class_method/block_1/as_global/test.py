from com.example import OuterClass

print("Outer class is", OuterClass)
obj1 = OuterClass()
obj1.method()

print("Inner class is", OuterClass.InnerClass)
obj2 = OuterClass.InnerClass()
obj2.method()

print("Done.")
