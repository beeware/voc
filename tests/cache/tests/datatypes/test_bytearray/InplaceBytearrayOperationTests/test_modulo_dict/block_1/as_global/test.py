try:
    print('>>> x = bytearray()')
    print('>>> y = {}')
    print('>>> x %= y')
    print('>>> x')
    x = bytearray()
    y = {}
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = bytearray()')
    print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> x %= y')
    print('>>> x')
    x = bytearray()
    y = {"a": 1, "c": 2.3456, "d": "another"}
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = bytearray(1)')
    print('>>> y = {}')
    print('>>> x %= y')
    print('>>> x')
    x = bytearray(1)
    y = {}
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = bytearray(1)')
    print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> x %= y')
    print('>>> x')
    x = bytearray(1)
    y = {"a": 1, "c": 2.3456, "d": "another"}
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = bytearray([1, 2, 3])')
    print('>>> y = {}')
    print('>>> x %= y')
    print('>>> x')
    x = bytearray([1, 2, 3])
    y = {}
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = bytearray([1, 2, 3])')
    print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> x %= y')
    print('>>> x')
    x = bytearray([1, 2, 3])
    y = {"a": 1, "c": 2.3456, "d": "another"}
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
