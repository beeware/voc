try:
    print('>>> x = b""')
    print('>>> y = True')
    print('>>> x |= y')
    print('>>> x')
    x = b""
    y = True
    x |= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = b""')
    print('>>> y = False')
    print('>>> x |= y')
    print('>>> x')
    x = b""
    y = False
    x |= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = b"This is another string of bytes"')
    print('>>> y = True')
    print('>>> x |= y')
    print('>>> x')
    x = b"This is another string of bytes"
    y = True
    x |= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = b"This is another string of bytes"')
    print('>>> y = False')
    print('>>> x |= y')
    print('>>> x')
    x = b"This is another string of bytes"
    y = False
    x |= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
