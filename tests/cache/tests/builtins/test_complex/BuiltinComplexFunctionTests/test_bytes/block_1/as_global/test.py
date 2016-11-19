try:
    print('>>> f = complex')
    print('>>> x = b""')
    print('>>> f(x)')
    f = complex
    x = b""
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = complex')
    print('>>> x = b"This is another string of bytes"')
    print('>>> f(x)')
    f = complex
    x = b"This is another string of bytes"
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
