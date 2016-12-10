try:
    print('>>> f = vars')
    print('>>> x = b""')
    print('>>> f(x)')
    f = vars
    x = b""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = vars')
    print('>>> x = b"This is another string of bytes"')
    print('>>> f(x)')
    f = vars
    x = b"This is another string of bytes"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
