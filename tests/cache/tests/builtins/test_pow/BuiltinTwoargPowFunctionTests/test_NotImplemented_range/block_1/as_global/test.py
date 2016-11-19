try:
    print('>>> f = pow')
    print('>>> x = NotImplemented')
    print('>>> y = range(0)')
    print('>>> f(x, y)')
    f = pow
    x = NotImplemented
    y = range(0)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = NotImplemented')
    print('>>> y = range(5)')
    print('>>> f(x, y)')
    f = pow
    x = NotImplemented
    y = range(5)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = NotImplemented')
    print('>>> y = range(2, 7)')
    print('>>> f(x, y)')
    f = pow
    x = NotImplemented
    y = range(2, 7)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = NotImplemented')
    print('>>> y = range(2, 7, 2)')
    print('>>> f(x, y)')
    f = pow
    x = NotImplemented
    y = range(2, 7, 2)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = NotImplemented')
    print('>>> y = range(7, 2, -1)')
    print('>>> f(x, y)')
    f = pow
    x = NotImplemented
    y = range(7, 2, -1)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = NotImplemented')
    print('>>> y = range(7, 2, -2)')
    print('>>> f(x, y)')
    f = pow
    x = NotImplemented
    y = range(7, 2, -2)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
