try:
    print('>>> f = hasattr')
    print('>>> x = {}')
    print('>>> y = b""')
    print('>>> f(x, y)')
    f = hasattr
    x = {}
    y = b""
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = {}')
    print('>>> y = b"This is another string of bytes"')
    print('>>> f(x, y)')
    f = hasattr
    x = {}
    y = b"This is another string of bytes"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = b""')
    print('>>> f(x, y)')
    f = hasattr
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = b""
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = b"This is another string of bytes"')
    print('>>> f(x, y)')
    f = hasattr
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = b"This is another string of bytes"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
