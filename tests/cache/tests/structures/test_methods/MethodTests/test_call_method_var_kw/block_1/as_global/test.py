class TestObj:
    def myfunc(self, *args, **kwargs):
        print(kwargs['first'] * 3)
        print(kwargs['second'] * 3)
        print(args)

        return kwargs['first'] + kwargs['second']

obj = TestObj()
values_tuple = (1, 2, 3, 4)
values_dict = {'first': 1, 'second': 2}
print("values sum =", obj.myfunc(*values_tuple, **values_dict))
print('Done.')
