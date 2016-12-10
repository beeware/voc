try:
    print('>>> x = {}')
    print('>>> y = bytearray()')
    print('>>> x / y')
    x = {}
    y = bytearray()
    print(x / y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {}')
    print('>>> y = bytearray(1)')
    print('>>> x / y')
    x = {}
    y = bytearray(1)
    print(x / y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {}')
    print('>>> y = bytearray([1, 2, 3])')
    print('>>> x / y')
    x = {}
    y = bytearray([1, 2, 3])
    print(x / y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = bytearray()')
    print('>>> x / y')
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = bytearray()
    print(x / y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = bytearray(1)')
    print('>>> x / y')
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = bytearray(1)
    print(x / y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = bytearray([1, 2, 3])')
    print('>>> x / y')
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = bytearray([1, 2, 3])
    print(x / y)
except Exception as e:
    print(type(e), ':', e)
print()
