try:
    print('>>> x = None')
    print('>>> y = frozenset()')
    print('>>> x == y')
    x = None
    y = frozenset()
    print(x == y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = None')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x == y')
    x = None
    y = frozenset({1, 2.3456, "another"})
    print(x == y)
except Exception as e:
    print(type(e), ':', e)
print()
