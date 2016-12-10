try:
    print('>>> x = frozenset()')
    print('>>> y = type(1)')
    print('>>> x < y')
    x = frozenset()
    y = type(1)
    print(x < y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset()')
    print('>>> y = type("a")')
    print('>>> x < y')
    x = frozenset()
    y = type("a")
    print(x < y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset()')
    print('>>> y = type(object())')
    print('>>> x < y')
    x = frozenset()
    y = type(object())
    print(x < y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset()')
    print('>>> y = type("MyClass", (object,), {})')
    print('>>> x < y')
    x = frozenset()
    y = type("MyClass", (object,), {})
    print(x < y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = type(1)')
    print('>>> x < y')
    x = frozenset({1, 2.3456, "another"})
    y = type(1)
    print(x < y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = type("a")')
    print('>>> x < y')
    x = frozenset({1, 2.3456, "another"})
    y = type("a")
    print(x < y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = type(object())')
    print('>>> x < y')
    x = frozenset({1, 2.3456, "another"})
    y = type(object())
    print(x < y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = type("MyClass", (object,), {})')
    print('>>> x < y')
    x = frozenset({1, 2.3456, "another"})
    y = type("MyClass", (object,), {})
    print(x < y)
except Exception as e:
    print(type(e), ':', e)
print()
