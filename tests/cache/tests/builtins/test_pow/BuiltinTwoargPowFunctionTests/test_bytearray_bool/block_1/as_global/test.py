try:
    print('>>> f = pow')
    print('>>> x = bytearray()')
    print('>>> y = True')
    print('>>> f(x, y)')
    f = pow
    x = bytearray()
    y = True
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = bytearray()')
    print('>>> y = False')
    print('>>> f(x, y)')
    f = pow
    x = bytearray()
    y = False
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = bytearray(1)')
    print('>>> y = True')
    print('>>> f(x, y)')
    f = pow
    x = bytearray(1)
    y = True
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = bytearray(1)')
    print('>>> y = False')
    print('>>> f(x, y)')
    f = pow
    x = bytearray(1)
    y = False
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = bytearray([1, 2, 3])')
    print('>>> y = True')
    print('>>> f(x, y)')
    f = pow
    x = bytearray([1, 2, 3])
    y = True
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = bytearray([1, 2, 3])')
    print('>>> y = False')
    print('>>> f(x, y)')
    f = pow
    x = bytearray([1, 2, 3])
    y = False
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
