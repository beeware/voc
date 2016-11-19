class TestObj:
    def myfunc(self, **kwargs):
        print(kwargs['first'] * 3)
        print(kwargs['second'] * 3)

        return kwargs['first'] + kwargs['second']

obj = TestObj()
values = {'first': 1, 'second': 2}
print("values sum =", obj.myfunc(**values))
print('Done.')
