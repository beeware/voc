try:
    print('>>> f = getattr')
    print('>>> x = type(1)')
    print('>>> y = type(1)')
    print('>>> f(x, y)')
    f = getattr
    x = type(1)
    y = type(1)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type(1)')
    print('>>> y = type("a")')
    print('>>> f(x, y)')
    f = getattr
    x = type(1)
    y = type("a")
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type(1)')
    print('>>> y = type(object())')
    print('>>> f(x, y)')
    f = getattr
    x = type(1)
    y = type(object())
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type(1)')
    print('>>> y = type("MyClass", (object,), {})')
    print('>>> f(x, y)')
    f = getattr
    x = type(1)
    y = type("MyClass", (object,), {})
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type("a")')
    print('>>> y = type(1)')
    print('>>> f(x, y)')
    f = getattr
    x = type("a")
    y = type(1)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type("a")')
    print('>>> y = type("a")')
    print('>>> f(x, y)')
    f = getattr
    x = type("a")
    y = type("a")
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type("a")')
    print('>>> y = type(object())')
    print('>>> f(x, y)')
    f = getattr
    x = type("a")
    y = type(object())
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type("a")')
    print('>>> y = type("MyClass", (object,), {})')
    print('>>> f(x, y)')
    f = getattr
    x = type("a")
    y = type("MyClass", (object,), {})
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type(object())')
    print('>>> y = type(1)')
    print('>>> f(x, y)')
    f = getattr
    x = type(object())
    y = type(1)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type(object())')
    print('>>> y = type("a")')
    print('>>> f(x, y)')
    f = getattr
    x = type(object())
    y = type("a")
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type(object())')
    print('>>> y = type(object())')
    print('>>> f(x, y)')
    f = getattr
    x = type(object())
    y = type(object())
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type(object())')
    print('>>> y = type("MyClass", (object,), {})')
    print('>>> f(x, y)')
    f = getattr
    x = type(object())
    y = type("MyClass", (object,), {})
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> y = type(1)')
    print('>>> f(x, y)')
    f = getattr
    x = type("MyClass", (object,), {})
    y = type(1)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> y = type("a")')
    print('>>> f(x, y)')
    f = getattr
    x = type("MyClass", (object,), {})
    y = type("a")
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> y = type(object())')
    print('>>> f(x, y)')
    f = getattr
    x = type("MyClass", (object,), {})
    y = type(object())
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> y = type("MyClass", (object,), {})')
    print('>>> f(x, y)')
    f = getattr
    x = type("MyClass", (object,), {})
    y = type("MyClass", (object,), {})
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
