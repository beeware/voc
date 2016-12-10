try:
    print('>>> f = hasattr')
    print('>>> x = set()')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = hasattr
    x = set()
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = hasattr
    x = {1, 2.3456, "another"}
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
