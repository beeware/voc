try:
    print('>>> f = hasattr')
    print('>>> x = set()')
    print('>>> y = frozenset()')
    print('>>> f(x, y)')
    f = hasattr
    x = set()
    y = frozenset()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = set()')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> f(x, y)')
    f = hasattr
    x = set()
    y = frozenset({1, 2.3456, "another"})
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = frozenset()')
    print('>>> f(x, y)')
    f = hasattr
    x = {1, 2.3456, "another"}
    y = frozenset()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> f(x, y)')
    f = hasattr
    x = {1, 2.3456, "another"}
    y = frozenset({1, 2.3456, "another"})
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
