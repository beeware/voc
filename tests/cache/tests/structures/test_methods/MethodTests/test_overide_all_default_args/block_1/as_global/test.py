class TestObj:
    def myfunc(self, x, y=1, z=2):
        print("x =", x)
        print("y =", y)
        print("z =", z)

obj = TestObj()
obj.myfunc(37, 42, 99)
print('Done.')
