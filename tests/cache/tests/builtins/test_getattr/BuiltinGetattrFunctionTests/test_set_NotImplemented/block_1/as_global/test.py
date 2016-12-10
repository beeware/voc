try:
    print('>>> f = getattr')
    print('>>> x = set()')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = getattr
    x = set()
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = getattr
    x = {1, 2.3456, "another"}
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
