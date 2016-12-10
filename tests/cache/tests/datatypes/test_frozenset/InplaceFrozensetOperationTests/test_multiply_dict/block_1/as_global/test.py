try:
    print('>>> x = frozenset()')
    print('>>> y = {}')
    print('>>> x *= y')
    print('>>> x')
    x = frozenset()
    y = {}
    x *= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset()')
    print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> x *= y')
    print('>>> x')
    x = frozenset()
    y = {"a": 1, "c": 2.3456, "d": "another"}
    x *= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = {}')
    print('>>> x *= y')
    print('>>> x')
    x = frozenset({1, 2.3456, "another"})
    y = {}
    x *= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> x *= y')
    print('>>> x')
    x = frozenset({1, 2.3456, "another"})
    y = {"a": 1, "c": 2.3456, "d": "another"}
    x *= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
