try:
    print('>>> x = frozenset()')
    print('>>> y = set()')
    print('>>> x < y')
    x = frozenset()
    y = set()
    print(x < y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset()')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> x < y')
    x = frozenset()
    y = {1, 2.3456, "another"}
    print(x < y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = set()')
    print('>>> x < y')
    x = frozenset({1, 2.3456, "another"})
    y = set()
    print(x < y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> x < y')
    x = frozenset({1, 2.3456, "another"})
    y = {1, 2.3456, "another"}
    print(x < y)
except Exception as e:
    print(type(e), ':', e)
print()
