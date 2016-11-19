try:
    print('>>> f = object')
    print('>>> x = bytearray()')
    print('>>> f(x)')
    f = object
    x = bytearray()
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = object')
    print('>>> x = bytearray(1)')
    print('>>> f(x)')
    f = object
    x = bytearray(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = object')
    print('>>> x = bytearray([1, 2, 3])')
    print('>>> f(x)')
    f = object
    x = bytearray([1, 2, 3])
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
