try:
    print('>>> f = hasattr')
    print('>>> x = NotImplemented')
    print('>>> y = True')
    print('>>> f(x, y)')
    f = hasattr
    x = NotImplemented
    y = True
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = NotImplemented')
    print('>>> y = False')
    print('>>> f(x, y)')
    f = hasattr
    x = NotImplemented
    y = False
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
