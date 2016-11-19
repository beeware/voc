try:
    print('>>> x = True')
    print('>>> y = bytearray()')
    print('>>> x /= y')
    print('>>> x')
    x = True
    y = bytearray()
    x /= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = True')
    print('>>> y = bytearray(1)')
    print('>>> x /= y')
    print('>>> x')
    x = True
    y = bytearray(1)
    x /= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = True')
    print('>>> y = bytearray([1, 2, 3])')
    print('>>> x /= y')
    print('>>> x')
    x = True
    y = bytearray([1, 2, 3])
    x /= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = False')
    print('>>> y = bytearray()')
    print('>>> x /= y')
    print('>>> x')
    x = False
    y = bytearray()
    x /= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = False')
    print('>>> y = bytearray(1)')
    print('>>> x /= y')
    print('>>> x')
    x = False
    y = bytearray(1)
    x /= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = False')
    print('>>> y = bytearray([1, 2, 3])')
    print('>>> x /= y')
    print('>>> x')
    x = False
    y = bytearray([1, 2, 3])
    x /= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
