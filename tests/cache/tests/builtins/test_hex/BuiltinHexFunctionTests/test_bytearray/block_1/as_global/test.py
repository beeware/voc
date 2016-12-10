try:
    print('>>> f = hex')
    print('>>> x = bytearray()')
    print('>>> f(x)')
    f = hex
    x = bytearray()
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hex')
    print('>>> x = bytearray(1)')
    print('>>> f(x)')
    f = hex
    x = bytearray(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hex')
    print('>>> x = bytearray([1, 2, 3])')
    print('>>> f(x)')
    f = hex
    x = bytearray([1, 2, 3])
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
