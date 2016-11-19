try:
    print('>>> x = frozenset()')
    print('>>> y = frozenset()')
    print('>>> x < y')
    x = frozenset()
    y = frozenset()
    print(x < y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset()')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x < y')
    x = frozenset()
    y = frozenset({1, 2.3456, "another"})
    print(x < y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = frozenset()')
    print('>>> x < y')
    x = frozenset({1, 2.3456, "another"})
    y = frozenset()
    print(x < y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x < y')
    x = frozenset({1, 2.3456, "another"})
    y = frozenset({1, 2.3456, "another"})
    print(x < y)
except Exception as e:
    print(type(e), ':', e)
print()
