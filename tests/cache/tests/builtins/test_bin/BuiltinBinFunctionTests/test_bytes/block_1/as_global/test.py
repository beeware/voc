try:
    print('>>> f = bin')
    print('>>> x = b""')
    print('>>> f(x)')
    f = bin
    x = b""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = bin')
    print('>>> x = b"This is another string of bytes"')
    print('>>> f(x)')
    f = bin
    x = b"This is another string of bytes"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
