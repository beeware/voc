def myfunc(**kwargs):
    print(kwargs['first'] * 3)
    print(kwargs['second'] * 3)

    return kwargs['first'] + kwargs['second']

print("values sum =", myfunc(first=1, second=2))
print('Done.')
