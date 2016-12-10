try:
    print('>>> f = map')
    print('>>> x = True')
    print('>>> y = bytearray()')
    print('>>> f(x, y)')
    f = map
    x = True
    y = bytearray()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = True')
    print('>>> y = bytearray(1)')
    print('>>> f(x, y)')
    f = map
    x = True
    y = bytearray(1)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = True')
    print('>>> y = bytearray([1, 2, 3])')
    print('>>> f(x, y)')
    f = map
    x = True
    y = bytearray([1, 2, 3])
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = False')
    print('>>> y = bytearray()')
    print('>>> f(x, y)')
    f = map
    x = False
    y = bytearray()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = False')
    print('>>> y = bytearray(1)')
    print('>>> f(x, y)')
    f = map
    x = False
    y = bytearray(1)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = False')
    print('>>> y = bytearray([1, 2, 3])')
    print('>>> f(x, y)')
    f = map
    x = False
    y = bytearray([1, 2, 3])
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
