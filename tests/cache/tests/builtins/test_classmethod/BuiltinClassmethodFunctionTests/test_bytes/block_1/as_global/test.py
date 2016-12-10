try:
    print('>>> f = classmethod')
    print('>>> x = b""')
    print('>>> f(x)')
    f = classmethod
    x = b""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = classmethod')
    print('>>> x = b"This is another string of bytes"')
    print('>>> f(x)')
    f = classmethod
    x = b"This is another string of bytes"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
