try:
    print('>>> f = hasattr')
    print('>>> x = True')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = hasattr
    x = True
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = False')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = hasattr
    x = False
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
