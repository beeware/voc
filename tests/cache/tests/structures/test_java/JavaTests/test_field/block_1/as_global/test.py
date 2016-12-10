from com.example import MyClass

print("Class is", MyClass)
obj1 = MyClass()
print("Field is", MyClass.field)
print("Field from instance is", obj1.field)
obj1.field = 37
print("Updated Field from instance is", obj1.field)
print("Done.")
