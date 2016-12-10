class TestObj:
    def myfunc(self, value):
        print(value * 3)
        return value + 5

obj = TestObj()
print("value =", obj.myfunc(5))
print('Done.')
