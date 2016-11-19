try:
    print('>>> f = divmod')
    print('>>> x = {}')
    print('>>> y = type(1)')
    print('>>> f(x, y)')
    f = divmod
    x = {}
    y = type(1)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = {}')
    print('>>> y = type("a")')
    print('>>> f(x, y)')
    f = divmod
    x = {}
    y = type("a")
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = {}')
    print('>>> y = type(object())')
    print('>>> f(x, y)')
    f = divmod
    x = {}
    y = type(object())
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = {}')
    print('>>> y = type("MyClass", (object,), {})')
    print('>>> f(x, y)')
    f = divmod
    x = {}
    y = type("MyClass", (object,), {})
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = type(1)')
    print('>>> f(x, y)')
    f = divmod
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = type(1)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = type("a")')
    print('>>> f(x, y)')
    f = divmod
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = type("a")
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = type(object())')
    print('>>> f(x, y)')
    f = divmod
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = type(object())
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = type("MyClass", (object,), {})')
    print('>>> f(x, y)')
    f = divmod
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = type("MyClass", (object,), {})
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
