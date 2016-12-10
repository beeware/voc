try:
    print('>>> x = frozenset()')
    print('>>> y = True')
    print('>>> x % y')
    x = frozenset()
    y = True
    print(x % y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset()')
    print('>>> y = False')
    print('>>> x % y')
    x = frozenset()
    y = False
    print(x % y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = True')
    print('>>> x % y')
    x = frozenset({1, 2.3456, "another"})
    y = True
    print(x % y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = False')
    print('>>> x % y')
    x = frozenset({1, 2.3456, "another"})
    y = False
    print(x % y)
except Exception as e:
    print(type(e), ':', e)
print()
