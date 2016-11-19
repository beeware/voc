try:
    print('>>> f = divmod')
    print('>>> x = b""')
    print('>>> y = type(1)')
    print('>>> f(x, y)')
    f = divmod
    x = b""
    y = type(1)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = b""')
    print('>>> y = type("a")')
    print('>>> f(x, y)')
    f = divmod
    x = b""
    y = type("a")
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = b""')
    print('>>> y = type(object())')
    print('>>> f(x, y)')
    f = divmod
    x = b""
    y = type(object())
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = b""')
    print('>>> y = type("MyClass", (object,), {})')
    print('>>> f(x, y)')
    f = divmod
    x = b""
    y = type("MyClass", (object,), {})
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = b"This is another string of bytes"')
    print('>>> y = type(1)')
    print('>>> f(x, y)')
    f = divmod
    x = b"This is another string of bytes"
    y = type(1)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = b"This is another string of bytes"')
    print('>>> y = type("a")')
    print('>>> f(x, y)')
    f = divmod
    x = b"This is another string of bytes"
    y = type("a")
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = b"This is another string of bytes"')
    print('>>> y = type(object())')
    print('>>> f(x, y)')
    f = divmod
    x = b"This is another string of bytes"
    y = type(object())
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = b"This is another string of bytes"')
    print('>>> y = type("MyClass", (object,), {})')
    print('>>> f(x, y)')
    f = divmod
    x = b"This is another string of bytes"
    y = type("MyClass", (object,), {})
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
