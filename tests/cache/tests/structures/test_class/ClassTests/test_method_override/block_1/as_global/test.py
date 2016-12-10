class MyObject:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return "Myobject instance %s" % self.x

obj = MyObject(37)

print(obj)
print('Done.')
