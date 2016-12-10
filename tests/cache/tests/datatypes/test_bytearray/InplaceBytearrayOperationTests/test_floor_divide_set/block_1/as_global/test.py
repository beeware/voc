try:
    print('>>> x = bytearray()')
    print('>>> y = set()')
    print('>>> x //= y')
    print('>>> x')
    x = bytearray()
    y = set()
    x //= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = bytearray()')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> x //= y')
    print('>>> x')
    x = bytearray()
    y = {1, 2.3456, "another"}
    x //= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = bytearray(1)')
    print('>>> y = set()')
    print('>>> x //= y')
    print('>>> x')
    x = bytearray(1)
    y = set()
    x //= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = bytearray(1)')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> x //= y')
    print('>>> x')
    x = bytearray(1)
    y = {1, 2.3456, "another"}
    x //= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = bytearray([1, 2, 3])')
    print('>>> y = set()')
    print('>>> x //= y')
    print('>>> x')
    x = bytearray([1, 2, 3])
    y = set()
    x //= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = bytearray([1, 2, 3])')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> x //= y')
    print('>>> x')
    x = bytearray([1, 2, 3])
    y = {1, 2.3456, "another"}
    x //= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
