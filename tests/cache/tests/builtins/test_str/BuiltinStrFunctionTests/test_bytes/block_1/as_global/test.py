try:
    print('>>> f = str')
    print('>>> x = b""')
    print('>>> f(x)')
    f = str
    x = b""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = str')
    print('>>> x = b"This is another string of bytes"')
    print('>>> f(x)')
    f = str
    x = b"This is another string of bytes"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
