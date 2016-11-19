try:
    print('>>> f = filter')
    print('>>> x = type(1)')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = filter
    x = type(1)
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = type("a")')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = filter
    x = type("a")
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = type(object())')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = filter
    x = type(object())
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = filter
    x = type("MyClass", (object,), {})
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
