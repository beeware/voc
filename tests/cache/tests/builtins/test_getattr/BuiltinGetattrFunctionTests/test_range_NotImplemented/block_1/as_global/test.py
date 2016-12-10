try:
    print('>>> f = getattr')
    print('>>> x = range(0)')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = getattr
    x = range(0)
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = range(5)')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = getattr
    x = range(5)
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = range(2, 7)')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = getattr
    x = range(2, 7)
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = range(2, 7, 2)')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = getattr
    x = range(2, 7, 2)
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = range(7, 2, -1)')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = getattr
    x = range(7, 2, -1)
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = range(7, 2, -2)')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = getattr
    x = range(7, 2, -2)
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
