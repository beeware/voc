try:
    print('>>> x = bytearray()')
    print('>>> y = bytearray()')
    print('>>> x **= y')
    print('>>> x')
    x = bytearray()
    y = bytearray()
    x **= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = bytearray()')
    print('>>> y = bytearray(1)')
    print('>>> x **= y')
    print('>>> x')
    x = bytearray()
    y = bytearray(1)
    x **= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = bytearray()')
    print('>>> y = bytearray([1, 2, 3])')
    print('>>> x **= y')
    print('>>> x')
    x = bytearray()
    y = bytearray([1, 2, 3])
    x **= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = bytearray(1)')
    print('>>> y = bytearray()')
    print('>>> x **= y')
    print('>>> x')
    x = bytearray(1)
    y = bytearray()
    x **= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = bytearray(1)')
    print('>>> y = bytearray(1)')
    print('>>> x **= y')
    print('>>> x')
    x = bytearray(1)
    y = bytearray(1)
    x **= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = bytearray(1)')
    print('>>> y = bytearray([1, 2, 3])')
    print('>>> x **= y')
    print('>>> x')
    x = bytearray(1)
    y = bytearray([1, 2, 3])
    x **= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = bytearray([1, 2, 3])')
    print('>>> y = bytearray()')
    print('>>> x **= y')
    print('>>> x')
    x = bytearray([1, 2, 3])
    y = bytearray()
    x **= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = bytearray([1, 2, 3])')
    print('>>> y = bytearray(1)')
    print('>>> x **= y')
    print('>>> x')
    x = bytearray([1, 2, 3])
    y = bytearray(1)
    x **= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = bytearray([1, 2, 3])')
    print('>>> y = bytearray([1, 2, 3])')
    print('>>> x **= y')
    print('>>> x')
    x = bytearray([1, 2, 3])
    y = bytearray([1, 2, 3])
    x **= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
