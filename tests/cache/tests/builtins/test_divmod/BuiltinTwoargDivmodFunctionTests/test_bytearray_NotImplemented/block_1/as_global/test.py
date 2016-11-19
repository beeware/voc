try:
    print('>>> f = divmod')
    print('>>> x = bytearray()')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = divmod
    x = bytearray()
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = bytearray(1)')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = divmod
    x = bytearray(1)
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = bytearray([1, 2, 3])')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = divmod
    x = bytearray([1, 2, 3])
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
