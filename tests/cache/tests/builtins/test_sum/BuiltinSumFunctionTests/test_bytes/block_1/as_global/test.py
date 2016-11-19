try:
    print('>>> f = sum')
    print('>>> x = b""')
    print('>>> f(x)')
    f = sum
    x = b""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = sum')
    print('>>> x = b"This is another string of bytes"')
    print('>>> f(x)')
    f = sum
    x = b"This is another string of bytes"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
