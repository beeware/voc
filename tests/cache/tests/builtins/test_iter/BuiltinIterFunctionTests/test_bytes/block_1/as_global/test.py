try:
    print('>>> f = iter')
    print('>>> x = b""')
    print('>>> f(x)')
    f = iter
    x = b""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = iter')
    print('>>> x = b"This is another string of bytes"')
    print('>>> f(x)')
    f = iter
    x = b"This is another string of bytes"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
