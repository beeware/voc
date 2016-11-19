from com.example import MyBase, MyClass

print("Base class is", MyBase)
print("Class is", MyClass)

print("Base method on superclass is", MyBase.base_method)
print("Method on superclass is", MyBase.method)

print("Base method is", MyClass.base_method)
print("Method is", MyClass.method)

obj1 = MyBase()
print("Base method from superclass instance is", obj1.base_method)
obj1.base_method()
print("Method from superclass instance is", obj1.method)
obj1.method()

obj2 = MyClass()
print("Base method from instance is", obj2.base_method)
obj2.base_method()
print("Method from instance is", obj2.method)
obj2.method()
print("Done.")
