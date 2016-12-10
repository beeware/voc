try:
    print('>>> f = getattr')
    print('>>> x = set()')
    print('>>> y = bytearray()')
    print('>>> f(x, y)')
    f = getattr
    x = set()
    y = bytearray()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = set()')
    print('>>> y = bytearray(1)')
    print('>>> f(x, y)')
    f = getattr
    x = set()
    y = bytearray(1)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = set()')
    print('>>> y = bytearray([1, 2, 3])')
    print('>>> f(x, y)')
    f = getattr
    x = set()
    y = bytearray([1, 2, 3])
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = bytearray()')
    print('>>> f(x, y)')
    f = getattr
    x = {1, 2.3456, "another"}
    y = bytearray()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = bytearray(1)')
    print('>>> f(x, y)')
    f = getattr
    x = {1, 2.3456, "another"}
    y = bytearray(1)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = bytearray([1, 2, 3])')
    print('>>> f(x, y)')
    f = getattr
    x = {1, 2.3456, "another"}
    y = bytearray([1, 2, 3])
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
