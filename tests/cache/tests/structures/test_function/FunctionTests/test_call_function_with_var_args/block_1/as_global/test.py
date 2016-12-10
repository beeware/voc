def myfunc(*args):
    print(args)
    return args[0]

print("first arg =", myfunc(1, 2, 3, 4, 5))
print('Done.')
