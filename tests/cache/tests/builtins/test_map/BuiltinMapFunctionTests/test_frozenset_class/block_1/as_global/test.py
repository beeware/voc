try:
    print('>>> f = map')
    print('>>> x = frozenset()')
    print('>>> y = type(1)')
    print('>>> f(x, y)')
    f = map
    x = frozenset()
    y = type(1)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = frozenset()')
    print('>>> y = type("a")')
    print('>>> f(x, y)')
    f = map
    x = frozenset()
    y = type("a")
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = frozenset()')
    print('>>> y = type(object())')
    print('>>> f(x, y)')
    f = map
    x = frozenset()
    y = type(object())
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = frozenset()')
    print('>>> y = type("MyClass", (object,), {})')
    print('>>> f(x, y)')
    f = map
    x = frozenset()
    y = type("MyClass", (object,), {})
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = type(1)')
    print('>>> f(x, y)')
    f = map
    x = frozenset({1, 2.3456, "another"})
    y = type(1)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = type("a")')
    print('>>> f(x, y)')
    f = map
    x = frozenset({1, 2.3456, "another"})
    y = type("a")
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = type(object())')
    print('>>> f(x, y)')
    f = map
    x = frozenset({1, 2.3456, "another"})
    y = type(object())
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = type("MyClass", (object,), {})')
    print('>>> f(x, y)')
    f = map
    x = frozenset({1, 2.3456, "another"})
    y = type("MyClass", (object,), {})
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
