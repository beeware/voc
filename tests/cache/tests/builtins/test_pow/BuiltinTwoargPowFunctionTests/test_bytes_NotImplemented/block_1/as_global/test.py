try:
    print('>>> f = pow')
    print('>>> x = b""')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = pow
    x = b""
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = b"This is another string of bytes"')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = pow
    x = b"This is another string of bytes"
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
