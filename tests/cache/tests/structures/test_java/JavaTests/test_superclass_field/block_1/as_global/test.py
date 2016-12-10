from com.example import MyBase, MyClass

print("Base class is", MyBase)
print("Class is", MyClass)
obj1 = MyClass()
print("Base field on superclass is", MyBase.base_field)
print("Base field is", MyClass.base_field)
print("Base field from instance is", obj1.base_field)
print("Field is", MyClass.field)
print("Field from instance is", obj1.field)
print("Done.")
