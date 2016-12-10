try:
    print('>>> f = map')
    print('>>> x = frozenset()')
    print('>>> y = True')
    print('>>> f(x, y)')
    f = map
    x = frozenset()
    y = True
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = frozenset()')
    print('>>> y = False')
    print('>>> f(x, y)')
    f = map
    x = frozenset()
    y = False
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = True')
    print('>>> f(x, y)')
    f = map
    x = frozenset({1, 2.3456, "another"})
    y = True
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = False')
    print('>>> f(x, y)')
    f = map
    x = frozenset({1, 2.3456, "another"})
    y = False
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
