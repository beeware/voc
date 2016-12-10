try:
    print('>>> f = pow')
    print('>>> x = {}')
    print('>>> y = bytearray()')
    print('>>> f(x, y)')
    f = pow
    x = {}
    y = bytearray()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = {}')
    print('>>> y = bytearray(1)')
    print('>>> f(x, y)')
    f = pow
    x = {}
    y = bytearray(1)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = {}')
    print('>>> y = bytearray([1, 2, 3])')
    print('>>> f(x, y)')
    f = pow
    x = {}
    y = bytearray([1, 2, 3])
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = bytearray()')
    print('>>> f(x, y)')
    f = pow
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = bytearray()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = bytearray(1)')
    print('>>> f(x, y)')
    f = pow
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = bytearray(1)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = bytearray([1, 2, 3])')
    print('>>> f(x, y)')
    f = pow
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = bytearray([1, 2, 3])
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
