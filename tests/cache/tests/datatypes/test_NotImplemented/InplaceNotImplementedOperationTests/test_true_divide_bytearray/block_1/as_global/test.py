try:
    print('>>> x = NotImplemented')
    print('>>> y = bytearray()')
    print('>>> x /= y')
    print('>>> x')
    x = NotImplemented
    y = bytearray()
    x /= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = NotImplemented')
    print('>>> y = bytearray(1)')
    print('>>> x /= y')
    print('>>> x')
    x = NotImplemented
    y = bytearray(1)
    x /= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = NotImplemented')
    print('>>> y = bytearray([1, 2, 3])')
    print('>>> x /= y')
    print('>>> x')
    x = NotImplemented
    y = bytearray([1, 2, 3])
    x /= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
