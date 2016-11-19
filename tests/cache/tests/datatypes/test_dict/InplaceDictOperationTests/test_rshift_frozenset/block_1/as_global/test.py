try:
    print('>>> x = {}')
    print('>>> y = frozenset()')
    print('>>> x >>= y')
    print('>>> x')
    x = {}
    y = frozenset()
    x >>= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {}')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x >>= y')
    print('>>> x')
    x = {}
    y = frozenset({1, 2.3456, "another"})
    x >>= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = frozenset()')
    print('>>> x >>= y')
    print('>>> x')
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = frozenset()
    x >>= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x >>= y')
    print('>>> x')
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = frozenset({1, 2.3456, "another"})
    x >>= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
