try:
    print('>>> f = map')
    print('>>> x = bytearray()')
    print('>>> y = b""')
    print('>>> f(x, y)')
    f = map
    x = bytearray()
    y = b""
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = bytearray()')
    print('>>> y = b"This is another string of bytes"')
    print('>>> f(x, y)')
    f = map
    x = bytearray()
    y = b"This is another string of bytes"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = bytearray(1)')
    print('>>> y = b""')
    print('>>> f(x, y)')
    f = map
    x = bytearray(1)
    y = b""
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = bytearray(1)')
    print('>>> y = b"This is another string of bytes"')
    print('>>> f(x, y)')
    f = map
    x = bytearray(1)
    y = b"This is another string of bytes"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = bytearray([1, 2, 3])')
    print('>>> y = b""')
    print('>>> f(x, y)')
    f = map
    x = bytearray([1, 2, 3])
    y = b""
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = bytearray([1, 2, 3])')
    print('>>> y = b"This is another string of bytes"')
    print('>>> f(x, y)')
    f = map
    x = bytearray([1, 2, 3])
    y = b"This is another string of bytes"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
