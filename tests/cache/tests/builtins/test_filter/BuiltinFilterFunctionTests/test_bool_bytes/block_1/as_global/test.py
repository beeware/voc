try:
    print('>>> f = filter')
    print('>>> x = True')
    print('>>> y = b""')
    print('>>> f(x, y)')
    f = filter
    x = True
    y = b""
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = True')
    print('>>> y = b"This is another string of bytes"')
    print('>>> f(x, y)')
    f = filter
    x = True
    y = b"This is another string of bytes"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = False')
    print('>>> y = b""')
    print('>>> f(x, y)')
    f = filter
    x = False
    y = b""
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = False')
    print('>>> y = b"This is another string of bytes"')
    print('>>> f(x, y)')
    f = filter
    x = False
    y = b"This is another string of bytes"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
