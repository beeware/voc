try:
    print('>>> f = any')
    print('>>> x = b""')
    print('>>> f(x)')
    f = any
    x = b""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = any')
    print('>>> x = b"This is another string of bytes"')
    print('>>> f(x)')
    f = any
    x = b"This is another string of bytes"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
