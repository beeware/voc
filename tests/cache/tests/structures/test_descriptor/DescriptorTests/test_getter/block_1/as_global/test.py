class MyObject:
    def getter(self):
        print("Got attribute")
        return 1234

    attr = property(getter)

obj = MyObject()
print("obj.attr =", obj.attr)

try:
    obj.attr = 2345
    print("Shouldn't be able to set attribute.")
except AttributeError:
    print("Couldn't set attribute.")

try:
    del obj.attr
    print("Shouldn't be able to delete attribute.")
except AttributeError:
    print("Couldn't delete attribute.")

print("Done.")
