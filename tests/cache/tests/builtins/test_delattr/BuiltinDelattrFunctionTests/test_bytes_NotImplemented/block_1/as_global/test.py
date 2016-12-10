try:
    print('>>> f = delattr')
    print('>>> x = b""')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = delattr
    x = b""
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = delattr')
    print('>>> x = b"This is another string of bytes"')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = delattr
    x = b"This is another string of bytes"
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
