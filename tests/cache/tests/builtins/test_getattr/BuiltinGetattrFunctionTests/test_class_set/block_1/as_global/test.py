try:
    print('>>> f = getattr')
    print('>>> x = type(1)')
    print('>>> y = set()')
    print('>>> f(x, y)')
    f = getattr
    x = type(1)
    y = set()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type(1)')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> f(x, y)')
    f = getattr
    x = type(1)
    y = {1, 2.3456, "another"}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type("a")')
    print('>>> y = set()')
    print('>>> f(x, y)')
    f = getattr
    x = type("a")
    y = set()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type("a")')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> f(x, y)')
    f = getattr
    x = type("a")
    y = {1, 2.3456, "another"}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type(object())')
    print('>>> y = set()')
    print('>>> f(x, y)')
    f = getattr
    x = type(object())
    y = set()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type(object())')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> f(x, y)')
    f = getattr
    x = type(object())
    y = {1, 2.3456, "another"}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> y = set()')
    print('>>> f(x, y)')
    f = getattr
    x = type("MyClass", (object,), {})
    y = set()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> f(x, y)')
    f = getattr
    x = type("MyClass", (object,), {})
    y = {1, 2.3456, "another"}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
