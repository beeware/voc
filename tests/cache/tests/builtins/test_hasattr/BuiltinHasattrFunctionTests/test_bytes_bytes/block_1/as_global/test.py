try:
    print('>>> f = hasattr')
    print('>>> x = b""')
    print('>>> y = b""')
    print('>>> f(x, y)')
    f = hasattr
    x = b""
    y = b""
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = b""')
    print('>>> y = b"This is another string of bytes"')
    print('>>> f(x, y)')
    f = hasattr
    x = b""
    y = b"This is another string of bytes"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = b"This is another string of bytes"')
    print('>>> y = b""')
    print('>>> f(x, y)')
    f = hasattr
    x = b"This is another string of bytes"
    y = b""
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = b"This is another string of bytes"')
    print('>>> y = b"This is another string of bytes"')
    print('>>> f(x, y)')
    f = hasattr
    x = b"This is another string of bytes"
    y = b"This is another string of bytes"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
