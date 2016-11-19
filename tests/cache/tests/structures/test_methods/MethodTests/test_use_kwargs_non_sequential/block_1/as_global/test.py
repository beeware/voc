class TestObj:
    def myfunc(self, x, y=1, z=2):
        print("x =", x)
        print("y =", y)
        print("z =", z)

obj = TestObj()
obj.myfunc(37, z=42)
print('Done.')
