try:
    print('>>> f = delattr')
    print('>>> x = set()')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = delattr
    x = set()
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = delattr')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = delattr
    x = {1, 2.3456, "another"}
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
