try:
    print('>>> f = hasattr')
    print('>>> x = type(1)')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = hasattr
    x = type(1)
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = type("a")')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = hasattr
    x = type("a")
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = type(object())')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = hasattr
    x = type(object())
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = hasattr
    x = type("MyClass", (object,), {})
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
