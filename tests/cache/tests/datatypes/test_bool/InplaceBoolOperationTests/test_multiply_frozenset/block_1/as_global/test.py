try:
    print('>>> x = True')
    print('>>> y = frozenset()')
    print('>>> x *= y')
    print('>>> x')
    x = True
    y = frozenset()
    x *= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = True')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x *= y')
    print('>>> x')
    x = True
    y = frozenset({1, 2.3456, "another"})
    x *= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = False')
    print('>>> y = frozenset()')
    print('>>> x *= y')
    print('>>> x')
    x = False
    y = frozenset()
    x *= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = False')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x *= y')
    print('>>> x')
    x = False
    y = frozenset({1, 2.3456, "another"})
    x *= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
