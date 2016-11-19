try:
    print('>>> x = True')
    print('>>> y = frozenset()')
    print('>>> x // y')
    x = True
    y = frozenset()
    print(x // y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = True')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x // y')
    x = True
    y = frozenset({1, 2.3456, "another"})
    print(x // y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = False')
    print('>>> y = frozenset()')
    print('>>> x // y')
    x = False
    y = frozenset()
    print(x // y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = False')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x // y')
    x = False
    y = frozenset({1, 2.3456, "another"})
    print(x // y)
except Exception as e:
    print(type(e), ':', e)
print()
