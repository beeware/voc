try:
    print('>>> f = map')
    print('>>> x = frozenset()')
    print('>>> y = {}')
    print('>>> f(x, y)')
    f = map
    x = frozenset()
    y = {}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = frozenset()')
    print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> f(x, y)')
    f = map
    x = frozenset()
    y = {"a": 1, "c": 2.3456, "d": "another"}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = {}')
    print('>>> f(x, y)')
    f = map
    x = frozenset({1, 2.3456, "another"})
    y = {}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> f(x, y)')
    f = map
    x = frozenset({1, 2.3456, "another"})
    y = {"a": 1, "c": 2.3456, "d": "another"}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
