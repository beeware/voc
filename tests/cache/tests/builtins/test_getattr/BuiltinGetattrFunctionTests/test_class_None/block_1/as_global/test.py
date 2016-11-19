try:
    print('>>> f = getattr')
    print('>>> x = type(1)')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = getattr
    x = type(1)
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type("a")')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = getattr
    x = type("a")
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type(object())')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = getattr
    x = type(object())
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = getattr
    x = type("MyClass", (object,), {})
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
