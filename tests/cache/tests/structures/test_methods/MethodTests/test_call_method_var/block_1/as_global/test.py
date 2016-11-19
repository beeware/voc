class TestObj:
    def myfunc(self, *args):
        print(args)

        return len(args)

obj = TestObj()
values_tuple = (1, 2, 3, 4)
print("values count =", obj.myfunc(*values_tuple))
print('Done.')
