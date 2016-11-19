try:
    print('>>> x = True')
    print('>>> y = bytearray()')
    print('>>> x & y')
    x = True
    y = bytearray()
    print(x & y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = True')
    print('>>> y = bytearray(1)')
    print('>>> x & y')
    x = True
    y = bytearray(1)
    print(x & y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = True')
    print('>>> y = bytearray([1, 2, 3])')
    print('>>> x & y')
    x = True
    y = bytearray([1, 2, 3])
    print(x & y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = False')
    print('>>> y = bytearray()')
    print('>>> x & y')
    x = False
    y = bytearray()
    print(x & y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = False')
    print('>>> y = bytearray(1)')
    print('>>> x & y')
    x = False
    y = bytearray(1)
    print(x & y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = False')
    print('>>> y = bytearray([1, 2, 3])')
    print('>>> x & y')
    x = False
    y = bytearray([1, 2, 3])
    print(x & y)
except Exception as e:
    print(type(e), ':', e)
print()
