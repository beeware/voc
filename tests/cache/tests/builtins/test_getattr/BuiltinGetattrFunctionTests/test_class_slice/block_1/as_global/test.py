try:
    print('>>> f = getattr')
    print('>>> x = type(1)')
    print('>>> y = slice(0)')
    print('>>> f(x, y)')
    f = getattr
    x = type(1)
    y = slice(0)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type(1)')
    print('>>> y = slice(5)')
    print('>>> f(x, y)')
    f = getattr
    x = type(1)
    y = slice(5)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type(1)')
    print('>>> y = slice(2, 7)')
    print('>>> f(x, y)')
    f = getattr
    x = type(1)
    y = slice(2, 7)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type(1)')
    print('>>> y = slice(2, 7, 2)')
    print('>>> f(x, y)')
    f = getattr
    x = type(1)
    y = slice(2, 7, 2)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type(1)')
    print('>>> y = slice(7, 2, -1)')
    print('>>> f(x, y)')
    f = getattr
    x = type(1)
    y = slice(7, 2, -1)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type(1)')
    print('>>> y = slice(7, 2, -2)')
    print('>>> f(x, y)')
    f = getattr
    x = type(1)
    y = slice(7, 2, -2)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type("a")')
    print('>>> y = slice(0)')
    print('>>> f(x, y)')
    f = getattr
    x = type("a")
    y = slice(0)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type("a")')
    print('>>> y = slice(5)')
    print('>>> f(x, y)')
    f = getattr
    x = type("a")
    y = slice(5)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type("a")')
    print('>>> y = slice(2, 7)')
    print('>>> f(x, y)')
    f = getattr
    x = type("a")
    y = slice(2, 7)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type("a")')
    print('>>> y = slice(2, 7, 2)')
    print('>>> f(x, y)')
    f = getattr
    x = type("a")
    y = slice(2, 7, 2)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type("a")')
    print('>>> y = slice(7, 2, -1)')
    print('>>> f(x, y)')
    f = getattr
    x = type("a")
    y = slice(7, 2, -1)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type("a")')
    print('>>> y = slice(7, 2, -2)')
    print('>>> f(x, y)')
    f = getattr
    x = type("a")
    y = slice(7, 2, -2)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type(object())')
    print('>>> y = slice(0)')
    print('>>> f(x, y)')
    f = getattr
    x = type(object())
    y = slice(0)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type(object())')
    print('>>> y = slice(5)')
    print('>>> f(x, y)')
    f = getattr
    x = type(object())
    y = slice(5)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type(object())')
    print('>>> y = slice(2, 7)')
    print('>>> f(x, y)')
    f = getattr
    x = type(object())
    y = slice(2, 7)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type(object())')
    print('>>> y = slice(2, 7, 2)')
    print('>>> f(x, y)')
    f = getattr
    x = type(object())
    y = slice(2, 7, 2)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type(object())')
    print('>>> y = slice(7, 2, -1)')
    print('>>> f(x, y)')
    f = getattr
    x = type(object())
    y = slice(7, 2, -1)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type(object())')
    print('>>> y = slice(7, 2, -2)')
    print('>>> f(x, y)')
    f = getattr
    x = type(object())
    y = slice(7, 2, -2)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> y = slice(0)')
    print('>>> f(x, y)')
    f = getattr
    x = type("MyClass", (object,), {})
    y = slice(0)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> y = slice(5)')
    print('>>> f(x, y)')
    f = getattr
    x = type("MyClass", (object,), {})
    y = slice(5)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> y = slice(2, 7)')
    print('>>> f(x, y)')
    f = getattr
    x = type("MyClass", (object,), {})
    y = slice(2, 7)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> y = slice(2, 7, 2)')
    print('>>> f(x, y)')
    f = getattr
    x = type("MyClass", (object,), {})
    y = slice(2, 7, 2)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> y = slice(7, 2, -1)')
    print('>>> f(x, y)')
    f = getattr
    x = type("MyClass", (object,), {})
    y = slice(7, 2, -1)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> y = slice(7, 2, -2)')
    print('>>> f(x, y)')
    f = getattr
    x = type("MyClass", (object,), {})
    y = slice(7, 2, -2)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
