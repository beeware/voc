try:
    print('>>> f = divmod')
    print('>>> x = bytearray()')
    print('>>> y = {}')
    print('>>> f(x, y)')
    f = divmod
    x = bytearray()
    y = {}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = bytearray()')
    print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> f(x, y)')
    f = divmod
    x = bytearray()
    y = {"a": 1, "c": 2.3456, "d": "another"}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = bytearray(1)')
    print('>>> y = {}')
    print('>>> f(x, y)')
    f = divmod
    x = bytearray(1)
    y = {}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = bytearray(1)')
    print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> f(x, y)')
    f = divmod
    x = bytearray(1)
    y = {"a": 1, "c": 2.3456, "d": "another"}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = bytearray([1, 2, 3])')
    print('>>> y = {}')
    print('>>> f(x, y)')
    f = divmod
    x = bytearray([1, 2, 3])
    y = {}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = bytearray([1, 2, 3])')
    print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> f(x, y)')
    f = divmod
    x = bytearray([1, 2, 3])
    y = {"a": 1, "c": 2.3456, "d": "another"}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
