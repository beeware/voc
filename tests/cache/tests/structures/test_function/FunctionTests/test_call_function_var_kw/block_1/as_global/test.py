def myfunc(*args, **kwargs):
    print(kwargs['first'] * 3)
    print(kwargs['second'] * 3)
    print(args)

    return kwargs['first'] + kwargs['second']

values_tuple = (1, 2, 3, 4)
values_dict = {'first': 1, 'second': 2}
print("values sum =", myfunc(*values_tuple, **values_dict))
print('Done.')
