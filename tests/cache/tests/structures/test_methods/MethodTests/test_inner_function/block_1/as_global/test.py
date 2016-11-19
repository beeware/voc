class TestObj:
    def myfunc(self, value):
        print(value * 3)

        def myinner(value2):
            print(value2 * 4)
            return value2 + 6

        print("inner value =", myinner(10))
        return value + 5

obj = TestObj()
print("outer =", obj.myfunc(5))
print('Done.')
