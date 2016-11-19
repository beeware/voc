try:
    print('>>> f = pow')
    print('>>> x = set()')
    print('>>> y = type(1)')
    print('>>> f(x, y)')
    f = pow
    x = set()
    y = type(1)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = set()')
    print('>>> y = type("a")')
    print('>>> f(x, y)')
    f = pow
    x = set()
    y = type("a")
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = set()')
    print('>>> y = type(object())')
    print('>>> f(x, y)')
    f = pow
    x = set()
    y = type(object())
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = set()')
    print('>>> y = type("MyClass", (object,), {})')
    print('>>> f(x, y)')
    f = pow
    x = set()
    y = type("MyClass", (object,), {})
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = type(1)')
    print('>>> f(x, y)')
    f = pow
    x = {1, 2.3456, "another"}
    y = type(1)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = type("a")')
    print('>>> f(x, y)')
    f = pow
    x = {1, 2.3456, "another"}
    y = type("a")
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = type(object())')
    print('>>> f(x, y)')
    f = pow
    x = {1, 2.3456, "another"}
    y = type(object())
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = type("MyClass", (object,), {})')
    print('>>> f(x, y)')
    f = pow
    x = {1, 2.3456, "another"}
    y = type("MyClass", (object,), {})
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
