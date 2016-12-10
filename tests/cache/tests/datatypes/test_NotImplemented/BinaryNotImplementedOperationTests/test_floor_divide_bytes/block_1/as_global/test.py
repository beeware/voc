try:
    print('>>> x = NotImplemented')
    print('>>> y = b""')
    print('>>> x // y')
    x = NotImplemented
    y = b""
    print(x // y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = NotImplemented')
    print('>>> y = b"This is another string of bytes"')
    print('>>> x // y')
    x = NotImplemented
    y = b"This is another string of bytes"
    print(x // y)
except Exception as e:
    print(type(e), ':', e)
print()
