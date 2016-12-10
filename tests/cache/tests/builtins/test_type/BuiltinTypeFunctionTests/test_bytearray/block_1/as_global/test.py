try:
    print('>>> f = type')
    print('>>> x = bytearray()')
    print('>>> f(x)')
    f = type
    x = bytearray()
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = type')
    print('>>> x = bytearray(1)')
    print('>>> f(x)')
    f = type
    x = bytearray(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = type')
    print('>>> x = bytearray([1, 2, 3])')
    print('>>> f(x)')
    f = type
    x = bytearray([1, 2, 3])
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
