try:
    print('>>> x = set()')
    print('>>> y = frozenset()')
    print('>>> x ^= y')
    print('>>> x')
    x = set()
    y = frozenset()
    x ^= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = set()')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x ^= y')
    print('>>> x')
    x = set()
    y = frozenset({1, 2.3456, "another"})
    x ^= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = frozenset()')
    print('>>> x ^= y')
    print('>>> x')
    x = {1, 2.3456, "another"}
    y = frozenset()
    x ^= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x ^= y')
    print('>>> x')
    x = {1, 2.3456, "another"}
    y = frozenset({1, 2.3456, "another"})
    x ^= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
