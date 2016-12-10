try:
    print('>>> x = b""')
    print('>>> -x')
    x = b""
    print(-x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = b"This is another string of bytes"')
    print('>>> -x')
    x = b"This is another string of bytes"
    print(-x)
except Exception as e:
    print(type(e), ':', e)
print()
