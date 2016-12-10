try:
    print('>>> x = set()')
    print('>>> y = b""')
    print('>>> x <<= y')
    print('>>> x')
    x = set()
    y = b""
    x <<= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = set()')
    print('>>> y = b"This is another string of bytes"')
    print('>>> x <<= y')
    print('>>> x')
    x = set()
    y = b"This is another string of bytes"
    x <<= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = b""')
    print('>>> x <<= y')
    print('>>> x')
    x = {1, 2.3456, "another"}
    y = b""
    x <<= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = b"This is another string of bytes"')
    print('>>> x <<= y')
    print('>>> x')
    x = {1, 2.3456, "another"}
    y = b"This is another string of bytes"
    x <<= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
