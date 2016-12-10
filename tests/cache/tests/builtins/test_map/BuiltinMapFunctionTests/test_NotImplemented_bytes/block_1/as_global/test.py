try:
    print('>>> f = map')
    print('>>> x = NotImplemented')
    print('>>> y = b""')
    print('>>> f(x, y)')
    f = map
    x = NotImplemented
    y = b""
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = NotImplemented')
    print('>>> y = b"This is another string of bytes"')
    print('>>> f(x, y)')
    f = map
    x = NotImplemented
    y = b"This is another string of bytes"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
