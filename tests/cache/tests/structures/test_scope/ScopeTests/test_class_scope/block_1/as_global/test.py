x = 1

class Foo:
    def __init__(self, y):
        print("1: y =", y)
        x = 2
        print("2: x =", x)
        self.z = y

    w = x
    v = abs(x)
    x = 4

print("3: x =", x)
f = Foo(3)
print("3: Foo.v =", Foo.v)
print("3: f.v =", f.v)
print("3: Foo.w =", Foo.w)
print("3: f.w =", f.w)
print("3: x =", x)
try:
    print("3: f.x =", f.x)
except AttributeError:
    pass
try:
    print("3: f.y =", f.y)
except AttributeError:
    pass
print("3: f.z =", f.z)
print('Done.')
