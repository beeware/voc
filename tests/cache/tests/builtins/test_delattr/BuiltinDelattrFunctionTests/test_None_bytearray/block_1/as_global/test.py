try:
    print('>>> f = delattr')
    print('>>> x = None')
    print('>>> y = bytearray()')
    print('>>> f(x, y)')
    f = delattr
    x = None
    y = bytearray()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = delattr')
    print('>>> x = None')
    print('>>> y = bytearray(1)')
    print('>>> f(x, y)')
    f = delattr
    x = None
    y = bytearray(1)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = delattr')
    print('>>> x = None')
    print('>>> y = bytearray([1, 2, 3])')
    print('>>> f(x, y)')
    f = delattr
    x = None
    y = bytearray([1, 2, 3])
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
