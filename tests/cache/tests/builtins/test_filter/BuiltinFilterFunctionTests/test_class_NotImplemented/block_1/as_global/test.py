try:
    print('>>> f = filter')
    print('>>> x = type(1)')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = filter
    x = type(1)
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = type("a")')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = filter
    x = type("a")
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = type(object())')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = filter
    x = type(object())
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = filter
    x = type("MyClass", (object,), {})
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
