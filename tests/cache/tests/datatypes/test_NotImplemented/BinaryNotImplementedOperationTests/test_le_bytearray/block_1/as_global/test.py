try:
    print('>>> x = NotImplemented')
    print('>>> y = bytearray()')
    print('>>> x <= y')
    x = NotImplemented
    y = bytearray()
    print(x <= y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = NotImplemented')
    print('>>> y = bytearray(1)')
    print('>>> x <= y')
    x = NotImplemented
    y = bytearray(1)
    print(x <= y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = NotImplemented')
    print('>>> y = bytearray([1, 2, 3])')
    print('>>> x <= y')
    x = NotImplemented
    y = bytearray([1, 2, 3])
    print(x <= y)
except Exception as e:
    print(type(e), ':', e)
print()
