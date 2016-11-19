try:
    print('>>> x = frozenset()')
    print('>>> y = set()')
    print('>>> x <<= y')
    print('>>> x')
    x = frozenset()
    y = set()
    x <<= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset()')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> x <<= y')
    print('>>> x')
    x = frozenset()
    y = {1, 2.3456, "another"}
    x <<= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = set()')
    print('>>> x <<= y')
    print('>>> x')
    x = frozenset({1, 2.3456, "another"})
    y = set()
    x <<= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> x <<= y')
    print('>>> x')
    x = frozenset({1, 2.3456, "another"})
    y = {1, 2.3456, "another"}
    x <<= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
