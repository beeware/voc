try:
    print('>>> f = pow')
    print('>>> x = b""')
    print('>>> f(x)')
    f = pow
    x = b""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = b"This is another string of bytes"')
    print('>>> f(x)')
    f = pow
    x = b"This is another string of bytes"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
