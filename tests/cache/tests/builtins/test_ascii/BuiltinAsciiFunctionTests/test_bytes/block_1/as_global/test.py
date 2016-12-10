try:
    print('>>> f = ascii')
    print('>>> x = b""')
    print('>>> f(x)')
    f = ascii
    x = b""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = ascii')
    print('>>> x = b"This is another string of bytes"')
    print('>>> f(x)')
    f = ascii
    x = b"This is another string of bytes"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
