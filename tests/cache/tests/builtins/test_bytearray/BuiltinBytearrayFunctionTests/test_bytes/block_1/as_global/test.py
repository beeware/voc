try:
    print('>>> f = bytearray')
    print('>>> x = b""')
    print('>>> f(x)')
    f = bytearray
    x = b""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = bytearray')
    print('>>> x = b"This is another string of bytes"')
    print('>>> f(x)')
    f = bytearray
    x = b"This is another string of bytes"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
