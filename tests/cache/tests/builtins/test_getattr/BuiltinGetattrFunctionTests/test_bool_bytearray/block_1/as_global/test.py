try:
    print('>>> f = getattr')
    print('>>> x = True')
    print('>>> y = bytearray()')
    print('>>> f(x, y)')
    f = getattr
    x = True
    y = bytearray()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = True')
    print('>>> y = bytearray(1)')
    print('>>> f(x, y)')
    f = getattr
    x = True
    y = bytearray(1)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = True')
    print('>>> y = bytearray([1, 2, 3])')
    print('>>> f(x, y)')
    f = getattr
    x = True
    y = bytearray([1, 2, 3])
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = False')
    print('>>> y = bytearray()')
    print('>>> f(x, y)')
    f = getattr
    x = False
    y = bytearray()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = False')
    print('>>> y = bytearray(1)')
    print('>>> f(x, y)')
    f = getattr
    x = False
    y = bytearray(1)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = False')
    print('>>> y = bytearray([1, 2, 3])')
    print('>>> f(x, y)')
    f = getattr
    x = False
    y = bytearray([1, 2, 3])
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
