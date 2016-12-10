try:
    print('>>> f = filter')
    print('>>> x = None')
    print('>>> y = b""')
    print('>>> f(x, y)')
    f = filter
    x = None
    y = b""
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = None')
    print('>>> y = b"This is another string of bytes"')
    print('>>> f(x, y)')
    f = filter
    x = None
    y = b"This is another string of bytes"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
