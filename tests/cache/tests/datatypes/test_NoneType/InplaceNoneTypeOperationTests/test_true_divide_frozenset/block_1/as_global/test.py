try:
    print('>>> x = None')
    print('>>> y = frozenset()')
    print('>>> x /= y')
    print('>>> x')
    x = None
    y = frozenset()
    x /= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = None')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x /= y')
    print('>>> x')
    x = None
    y = frozenset({1, 2.3456, "another"})
    x /= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
