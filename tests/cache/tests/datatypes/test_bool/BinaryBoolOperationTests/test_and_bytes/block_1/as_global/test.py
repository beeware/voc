try:
    print('>>> x = True')
    print('>>> y = b""')
    print('>>> x & y')
    x = True
    y = b""
    print(x & y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = True')
    print('>>> y = b"This is another string of bytes"')
    print('>>> x & y')
    x = True
    y = b"This is another string of bytes"
    print(x & y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = False')
    print('>>> y = b""')
    print('>>> x & y')
    x = False
    y = b""
    print(x & y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = False')
    print('>>> y = b"This is another string of bytes"')
    print('>>> x & y')
    x = False
    y = b"This is another string of bytes"
    print(x & y)
except Exception as e:
    print(type(e), ':', e)
print()
