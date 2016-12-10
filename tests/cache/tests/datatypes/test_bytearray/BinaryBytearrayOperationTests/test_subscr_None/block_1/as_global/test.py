try:
    print('>>> x = bytearray()')
    print('>>> y = None')
    print('>>> x[y]')
    x = bytearray()
    y = None
    print(x[y])
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = bytearray(1)')
    print('>>> y = None')
    print('>>> x[y]')
    x = bytearray(1)
    y = None
    print(x[y])
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = bytearray([1, 2, 3])')
    print('>>> y = None')
    print('>>> x[y]')
    x = bytearray([1, 2, 3])
    y = None
    print(x[y])
except Exception as e:
    print(type(e), ':', e)
print()
