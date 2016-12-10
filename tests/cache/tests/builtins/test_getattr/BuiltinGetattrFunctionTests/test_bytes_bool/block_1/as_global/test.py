try:
    print('>>> f = getattr')
    print('>>> x = b""')
    print('>>> y = True')
    print('>>> f(x, y)')
    f = getattr
    x = b""
    y = True
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = b""')
    print('>>> y = False')
    print('>>> f(x, y)')
    f = getattr
    x = b""
    y = False
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = b"This is another string of bytes"')
    print('>>> y = True')
    print('>>> f(x, y)')
    f = getattr
    x = b"This is another string of bytes"
    y = True
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = b"This is another string of bytes"')
    print('>>> y = False')
    print('>>> f(x, y)')
    f = getattr
    x = b"This is another string of bytes"
    y = False
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
