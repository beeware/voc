try:
    print('>>> f = object')
    print('>>> x = b""')
    print('>>> f(x)')
    f = object
    x = b""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = object')
    print('>>> x = b"This is another string of bytes"')
    print('>>> f(x)')
    f = object
    x = b"This is another string of bytes"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
