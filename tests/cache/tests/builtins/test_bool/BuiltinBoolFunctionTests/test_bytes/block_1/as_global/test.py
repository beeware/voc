try:
    print('>>> f = bool')
    print('>>> x = b""')
    print('>>> f(x)')
    f = bool
    x = b""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = bool')
    print('>>> x = b"This is another string of bytes"')
    print('>>> f(x)')
    f = bool
    x = b"This is another string of bytes"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
