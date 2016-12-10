try:
    print('>>> f = pow')
    print('>>> x = bytearray()')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = pow
    x = bytearray()
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = bytearray(1)')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = pow
    x = bytearray(1)
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = bytearray([1, 2, 3])')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = pow
    x = bytearray([1, 2, 3])
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
