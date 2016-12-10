try:
    print('>>> f = bytes')
    print('>>> x = b""')
    print('>>> f(x)')
    f = bytes
    x = b""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = bytes')
    print('>>> x = b"This is another string of bytes"')
    print('>>> f(x)')
    f = bytes
    x = b"This is another string of bytes"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
