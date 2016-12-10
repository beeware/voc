try:
    print('>>> f = abs')
    print('>>> x = b""')
    print('>>> f(x)')
    f = abs
    x = b""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = abs')
    print('>>> x = b"This is another string of bytes"')
    print('>>> f(x)')
    f = abs
    x = b"This is another string of bytes"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
