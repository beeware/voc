try:
    print('>>> f = int')
    print('>>> x = b""')
    print('>>> f(x)')
    f = int
    x = b""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = int')
    print('>>> x = b"This is another string of bytes"')
    print('>>> f(x)')
    f = int
    x = b"This is another string of bytes"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
