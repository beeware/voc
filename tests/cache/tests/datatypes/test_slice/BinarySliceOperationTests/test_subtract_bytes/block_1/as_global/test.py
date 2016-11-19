try:
    print('>>> x = slice(0)')
    print('>>> y = b""')
    print('>>> x - y')
    x = slice(0)
    y = b""
    print(x - y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(0)')
    print('>>> y = b"This is another string of bytes"')
    print('>>> x - y')
    x = slice(0)
    y = b"This is another string of bytes"
    print(x - y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(5)')
    print('>>> y = b""')
    print('>>> x - y')
    x = slice(5)
    y = b""
    print(x - y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(5)')
    print('>>> y = b"This is another string of bytes"')
    print('>>> x - y')
    x = slice(5)
    y = b"This is another string of bytes"
    print(x - y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(2, 7)')
    print('>>> y = b""')
    print('>>> x - y')
    x = slice(2, 7)
    y = b""
    print(x - y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(2, 7)')
    print('>>> y = b"This is another string of bytes"')
    print('>>> x - y')
    x = slice(2, 7)
    y = b"This is another string of bytes"
    print(x - y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(2, 7, 2)')
    print('>>> y = b""')
    print('>>> x - y')
    x = slice(2, 7, 2)
    y = b""
    print(x - y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(2, 7, 2)')
    print('>>> y = b"This is another string of bytes"')
    print('>>> x - y')
    x = slice(2, 7, 2)
    y = b"This is another string of bytes"
    print(x - y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(7, 2, -1)')
    print('>>> y = b""')
    print('>>> x - y')
    x = slice(7, 2, -1)
    y = b""
    print(x - y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(7, 2, -1)')
    print('>>> y = b"This is another string of bytes"')
    print('>>> x - y')
    x = slice(7, 2, -1)
    y = b"This is another string of bytes"
    print(x - y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(7, 2, -2)')
    print('>>> y = b""')
    print('>>> x - y')
    x = slice(7, 2, -2)
    y = b""
    print(x - y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(7, 2, -2)')
    print('>>> y = b"This is another string of bytes"')
    print('>>> x - y')
    x = slice(7, 2, -2)
    y = b"This is another string of bytes"
    print(x - y)
except Exception as e:
    print(type(e), ':', e)
print()
