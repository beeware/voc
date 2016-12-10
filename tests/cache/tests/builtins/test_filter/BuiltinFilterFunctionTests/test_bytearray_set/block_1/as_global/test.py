try:
    print('>>> f = filter')
    print('>>> x = bytearray()')
    print('>>> y = set()')
    print('>>> f(x, y)')
    f = filter
    x = bytearray()
    y = set()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = bytearray()')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> f(x, y)')
    f = filter
    x = bytearray()
    y = {1, 2.3456, "another"}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = bytearray(1)')
    print('>>> y = set()')
    print('>>> f(x, y)')
    f = filter
    x = bytearray(1)
    y = set()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = bytearray(1)')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> f(x, y)')
    f = filter
    x = bytearray(1)
    y = {1, 2.3456, "another"}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = bytearray([1, 2, 3])')
    print('>>> y = set()')
    print('>>> f(x, y)')
    f = filter
    x = bytearray([1, 2, 3])
    y = set()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = bytearray([1, 2, 3])')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> f(x, y)')
    f = filter
    x = bytearray([1, 2, 3])
    y = {1, 2.3456, "another"}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
