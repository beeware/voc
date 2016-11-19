try:
    print('>>> x = b""')
    print('>>> y = b""')
    print('>>> x | y')
    x = b""
    y = b""
    print(x | y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = b""')
    print('>>> y = b"This is another string of bytes"')
    print('>>> x | y')
    x = b""
    y = b"This is another string of bytes"
    print(x | y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = b"This is another string of bytes"')
    print('>>> y = b""')
    print('>>> x | y')
    x = b"This is another string of bytes"
    y = b""
    print(x | y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = b"This is another string of bytes"')
    print('>>> y = b"This is another string of bytes"')
    print('>>> x | y')
    x = b"This is another string of bytes"
    y = b"This is another string of bytes"
    print(x | y)
except Exception as e:
    print(type(e), ':', e)
print()
