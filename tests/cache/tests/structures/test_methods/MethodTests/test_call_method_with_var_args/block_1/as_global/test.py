class TestObj:
    def myfunc(self, *args):
        print(args)
        return args[0]

obj = TestObj()
print("first arg =", obj.myfunc(1, 2, 3, 4, 5))
print('Done.')
