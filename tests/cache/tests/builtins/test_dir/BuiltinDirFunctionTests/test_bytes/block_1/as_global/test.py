try:
    print('>>> f = dir')
    print('>>> x = b""')
    print('>>> f(x)')
    f = dir
    x = b""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = dir')
    print('>>> x = b"This is another string of bytes"')
    print('>>> f(x)')
    f = dir
    x = b"This is another string of bytes"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
