try:
    print('>>> f = enumerate')
    print('>>> x = b""')
    print('>>> f(x)')
    f = enumerate
    x = b""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = enumerate')
    print('>>> x = b"This is another string of bytes"')
    print('>>> f(x)')
    f = enumerate
    x = b"This is another string of bytes"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
