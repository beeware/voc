try:
    print('>>> f = next')
    print('>>> x = b""')
    print('>>> f(x)')
    f = next
    x = b""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = next')
    print('>>> x = b"This is another string of bytes"')
    print('>>> f(x)')
    f = next
    x = b"This is another string of bytes"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
