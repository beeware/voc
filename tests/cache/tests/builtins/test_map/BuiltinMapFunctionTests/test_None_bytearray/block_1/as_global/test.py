try:
    print('>>> f = map')
    print('>>> x = None')
    print('>>> y = bytearray()')
    print('>>> f(x, y)')
    f = map
    x = None
    y = bytearray()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = None')
    print('>>> y = bytearray(1)')
    print('>>> f(x, y)')
    f = map
    x = None
    y = bytearray(1)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = None')
    print('>>> y = bytearray([1, 2, 3])')
    print('>>> f(x, y)')
    f = map
    x = None
    y = bytearray([1, 2, 3])
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
