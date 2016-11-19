try:
    print('>>> f = compile')
    print('>>> x = b""')
    print('>>> f(x)')
    f = compile
    x = b""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = compile')
    print('>>> x = b"This is another string of bytes"')
    print('>>> f(x)')
    f = compile
    x = b"This is another string of bytes"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
