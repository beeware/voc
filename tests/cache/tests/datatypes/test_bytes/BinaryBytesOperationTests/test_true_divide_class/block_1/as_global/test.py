try:
    print('>>> x = b""')
    print('>>> y = type(1)')
    print('>>> x / y')
    x = b""
    y = type(1)
    print(x / y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = b""')
    print('>>> y = type("a")')
    print('>>> x / y')
    x = b""
    y = type("a")
    print(x / y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = b""')
    print('>>> y = type(object())')
    print('>>> x / y')
    x = b""
    y = type(object())
    print(x / y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = b""')
    print('>>> y = type("MyClass", (object,), {})')
    print('>>> x / y')
    x = b""
    y = type("MyClass", (object,), {})
    print(x / y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = b"This is another string of bytes"')
    print('>>> y = type(1)')
    print('>>> x / y')
    x = b"This is another string of bytes"
    y = type(1)
    print(x / y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = b"This is another string of bytes"')
    print('>>> y = type("a")')
    print('>>> x / y')
    x = b"This is another string of bytes"
    y = type("a")
    print(x / y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = b"This is another string of bytes"')
    print('>>> y = type(object())')
    print('>>> x / y')
    x = b"This is another string of bytes"
    y = type(object())
    print(x / y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = b"This is another string of bytes"')
    print('>>> y = type("MyClass", (object,), {})')
    print('>>> x / y')
    x = b"This is another string of bytes"
    y = type("MyClass", (object,), {})
    print(x / y)
except Exception as e:
    print(type(e), ':', e)
print()
