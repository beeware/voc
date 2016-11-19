try:
    print('>>> f = range')
    print('>>> x = b""')
    print('>>> f(x)')
    f = range
    x = b""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = range')
    print('>>> x = b"This is another string of bytes"')
    print('>>> f(x)')
    f = range
    x = b"This is another string of bytes"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
