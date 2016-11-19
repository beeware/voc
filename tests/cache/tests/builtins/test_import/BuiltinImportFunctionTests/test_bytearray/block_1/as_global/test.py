try:
    print('>>> f = __import__')
    print('>>> x = bytearray()')
    print('>>> f(x)')
    f = __import__
    x = bytearray()
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = __import__')
    print('>>> x = bytearray(1)')
    print('>>> f(x)')
    f = __import__
    x = bytearray(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = __import__')
    print('>>> x = bytearray([1, 2, 3])')
    print('>>> f(x)')
    f = __import__
    x = bytearray([1, 2, 3])
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
