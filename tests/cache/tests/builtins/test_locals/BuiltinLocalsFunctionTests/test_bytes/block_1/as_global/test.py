try:
    print('>>> f = locals')
    print('>>> x = b""')
    print('>>> f(x)')
    f = locals
    x = b""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = locals')
    print('>>> x = b"This is another string of bytes"')
    print('>>> f(x)')
    f = locals
    x = b"This is another string of bytes"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
