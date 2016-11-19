try:
    print('>>> x = bytearray()')
    print('>>> y = NotImplemented')
    print('>>> x >> y')
    x = bytearray()
    y = NotImplemented
    print(x >> y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = bytearray(1)')
    print('>>> y = NotImplemented')
    print('>>> x >> y')
    x = bytearray(1)
    y = NotImplemented
    print(x >> y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = bytearray([1, 2, 3])')
    print('>>> y = NotImplemented')
    print('>>> x >> y')
    x = bytearray([1, 2, 3])
    y = NotImplemented
    print(x >> y)
except Exception as e:
    print(type(e), ':', e)
print()
