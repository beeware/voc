from com.example import MyClass

print("Class is", MyClass)
obj1 = MyClass()
print("Static constant is", MyClass.STATIC_CONSTANT)
print("Static constant from instance is", obj1.STATIC_CONSTANT)
print("Done.")
