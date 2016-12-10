try:
    print('>>> f = sorted')
    print('>>> x = b""')
    print('>>> f(x)')
    f = sorted
    x = b""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = sorted')
    print('>>> x = b"This is another string of bytes"')
    print('>>> f(x)')
    f = sorted
    x = b"This is another string of bytes"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
