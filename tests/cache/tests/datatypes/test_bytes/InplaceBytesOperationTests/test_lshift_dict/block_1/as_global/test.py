try:
    print('>>> x = b""')
    print('>>> y = {}')
    print('>>> x <<= y')
    print('>>> x')
    x = b""
    y = {}
    x <<= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = b""')
    print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> x <<= y')
    print('>>> x')
    x = b""
    y = {"a": 1, "c": 2.3456, "d": "another"}
    x <<= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = b"This is another string of bytes"')
    print('>>> y = {}')
    print('>>> x <<= y')
    print('>>> x')
    x = b"This is another string of bytes"
    y = {}
    x <<= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = b"This is another string of bytes"')
    print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> x <<= y')
    print('>>> x')
    x = b"This is another string of bytes"
    y = {"a": 1, "c": 2.3456, "d": "another"}
    x <<= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
