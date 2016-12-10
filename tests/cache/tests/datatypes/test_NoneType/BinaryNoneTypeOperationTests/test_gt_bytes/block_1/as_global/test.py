try:
    print('>>> x = None')
    print('>>> y = b""')
    print('>>> x > y')
    x = None
    y = b""
    print(x > y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = None')
    print('>>> y = b"This is another string of bytes"')
    print('>>> x > y')
    x = None
    y = b"This is another string of bytes"
    print(x > y)
except Exception as e:
    print(type(e), ':', e)
print()
