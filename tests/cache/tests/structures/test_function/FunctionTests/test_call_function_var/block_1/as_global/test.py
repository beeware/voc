def myfunc(*args):
    print(args)

    return len(args)

values_tuple = (1, 2, 3, 4)
print("values count =", myfunc(*values_tuple))
print('Done.')
