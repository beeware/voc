try:
    print('>>> x = b""')
    print('>>> y = None')
    print('>>> x &= y')
    print('>>> x')
    x = b""
    y = None
    x &= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = b"This is another string of bytes"')
    print('>>> y = None')
    print('>>> x &= y')
    print('>>> x')
    x = b"This is another string of bytes"
    y = None
    x &= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
