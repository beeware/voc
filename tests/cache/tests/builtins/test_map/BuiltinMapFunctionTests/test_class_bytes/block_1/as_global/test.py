try:
    print('>>> f = map')
    print('>>> x = type(1)')
    print('>>> y = b""')
    print('>>> f(x, y)')
    f = map
    x = type(1)
    y = b""
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = type(1)')
    print('>>> y = b"This is another string of bytes"')
    print('>>> f(x, y)')
    f = map
    x = type(1)
    y = b"This is another string of bytes"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = type("a")')
    print('>>> y = b""')
    print('>>> f(x, y)')
    f = map
    x = type("a")
    y = b""
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = type("a")')
    print('>>> y = b"This is another string of bytes"')
    print('>>> f(x, y)')
    f = map
    x = type("a")
    y = b"This is another string of bytes"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = type(object())')
    print('>>> y = b""')
    print('>>> f(x, y)')
    f = map
    x = type(object())
    y = b""
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = type(object())')
    print('>>> y = b"This is another string of bytes"')
    print('>>> f(x, y)')
    f = map
    x = type(object())
    y = b"This is another string of bytes"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> y = b""')
    print('>>> f(x, y)')
    f = map
    x = type("MyClass", (object,), {})
    y = b""
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> y = b"This is another string of bytes"')
    print('>>> f(x, y)')
    f = map
    x = type("MyClass", (object,), {})
    y = b"This is another string of bytes"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
