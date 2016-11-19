class TestObj:
    def myfunc(self, x, y=1, z=2):
        print("x =", x)
        print("y =", y)
        print("z =", z)

obj = TestObj()
obj.myfunc(z=99, y=42, x=37)
print('Done.')
