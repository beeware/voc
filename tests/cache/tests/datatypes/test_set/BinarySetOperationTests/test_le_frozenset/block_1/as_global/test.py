try:
    print('>>> x = set()')
    print('>>> y = frozenset()')
    print('>>> x <= y')
    x = set()
    y = frozenset()
    print(x <= y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = set()')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x <= y')
    x = set()
    y = frozenset({1, 2.3456, "another"})
    print(x <= y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = frozenset()')
    print('>>> x <= y')
    x = {1, 2.3456, "another"}
    y = frozenset()
    print(x <= y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x <= y')
    x = {1, 2.3456, "another"}
    y = frozenset({1, 2.3456, "another"})
    print(x <= y)
except Exception as e:
    print(type(e), ':', e)
print()
