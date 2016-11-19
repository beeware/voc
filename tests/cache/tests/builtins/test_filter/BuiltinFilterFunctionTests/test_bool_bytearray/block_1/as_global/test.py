try:
    print('>>> f = filter')
    print('>>> x = True')
    print('>>> y = bytearray()')
    print('>>> f(x, y)')
    f = filter
    x = True
    y = bytearray()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = True')
    print('>>> y = bytearray(1)')
    print('>>> f(x, y)')
    f = filter
    x = True
    y = bytearray(1)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = True')
    print('>>> y = bytearray([1, 2, 3])')
    print('>>> f(x, y)')
    f = filter
    x = True
    y = bytearray([1, 2, 3])
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = False')
    print('>>> y = bytearray()')
    print('>>> f(x, y)')
    f = filter
    x = False
    y = bytearray()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = False')
    print('>>> y = bytearray(1)')
    print('>>> f(x, y)')
    f = filter
    x = False
    y = bytearray(1)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = False')
    print('>>> y = bytearray([1, 2, 3])')
    print('>>> f(x, y)')
    f = filter
    x = False
    y = bytearray([1, 2, 3])
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
