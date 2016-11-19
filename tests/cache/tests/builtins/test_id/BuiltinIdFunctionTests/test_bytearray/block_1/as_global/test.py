try:
    print('>>> f = id')
    print('>>> x = bytearray()')
    print('>>> f(x)')
    f = id
    x = bytearray()
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = id')
    print('>>> x = bytearray(1)')
    print('>>> f(x)')
    f = id
    x = bytearray(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = id')
    print('>>> x = bytearray([1, 2, 3])')
    print('>>> f(x)')
    f = id
    x = bytearray([1, 2, 3])
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
