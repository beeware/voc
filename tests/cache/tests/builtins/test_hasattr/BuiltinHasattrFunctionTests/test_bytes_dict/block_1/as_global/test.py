try:
    print('>>> f = hasattr')
    print('>>> x = b""')
    print('>>> y = {}')
    print('>>> f(x, y)')
    f = hasattr
    x = b""
    y = {}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = b""')
    print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> f(x, y)')
    f = hasattr
    x = b""
    y = {"a": 1, "c": 2.3456, "d": "another"}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = b"This is another string of bytes"')
    print('>>> y = {}')
    print('>>> f(x, y)')
    f = hasattr
    x = b"This is another string of bytes"
    y = {}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = b"This is another string of bytes"')
    print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> f(x, y)')
    f = hasattr
    x = b"This is another string of bytes"
    y = {"a": 1, "c": 2.3456, "d": "another"}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
