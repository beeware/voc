class MyObject:
    def __init__(self):
        self.attr1 = 123

obj = MyObject()

obj.attr2 = 456
print('obj.attr1 =', obj.attr1)
print('obj.attr2 =', obj.attr2)

print("Delete attributes...")
del obj.attr1
del obj.attr2

print("Access deleted attributes...")
try:
    print('obj.attr1 = ', obj.attr1)
    print("obj.attr1 shouldn't exist")
except AttributeError:
    print("obj.attr1 doesn't exist")

try:
    print('obj.attr2 = ', obj.attr2)
    print("obj.attr2 shouldn't exist")
except AttributeError:
    print("obj.attr2 doesn't exist")

print("Delete deleted attributes...")
try:
    del obj.attr1
    print("obj.attr1 shouldn't existed")
except AttributeError:
    print("obj.attr1 doesn't exist")

try:
    del obj.attr2
    print("obj.attr2 shouldn't existed")
except AttributeError:
    print("obj.attr2 doesn't exist")

print("Delete non-existent attribute...")
try:
    del obj.no_such_attr
    print("obj.no_such_attr never existed")
except AttributeError:
    print("obj.no_such_attr doesn't exist")

print("Done.")
