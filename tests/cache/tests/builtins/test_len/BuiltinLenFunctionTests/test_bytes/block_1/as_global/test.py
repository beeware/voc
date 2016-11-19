try:
    print('>>> f = len')
    print('>>> x = b""')
    print('>>> f(x)')
    f = len
    x = b""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = len')
    print('>>> x = b"This is another string of bytes"')
    print('>>> f(x)')
    f = len
    x = b"This is another string of bytes"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
