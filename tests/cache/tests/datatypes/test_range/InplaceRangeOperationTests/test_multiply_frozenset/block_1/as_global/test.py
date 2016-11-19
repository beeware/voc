try:
    print('>>> x = range(0)')
    print('>>> y = frozenset()')
    print('>>> x *= y')
    print('>>> x')
    x = range(0)
    y = frozenset()
    x *= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = range(0)')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x *= y')
    print('>>> x')
    x = range(0)
    y = frozenset({1, 2.3456, "another"})
    x *= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = range(5)')
    print('>>> y = frozenset()')
    print('>>> x *= y')
    print('>>> x')
    x = range(5)
    y = frozenset()
    x *= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = range(5)')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x *= y')
    print('>>> x')
    x = range(5)
    y = frozenset({1, 2.3456, "another"})
    x *= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = range(2, 7)')
    print('>>> y = frozenset()')
    print('>>> x *= y')
    print('>>> x')
    x = range(2, 7)
    y = frozenset()
    x *= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = range(2, 7)')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x *= y')
    print('>>> x')
    x = range(2, 7)
    y = frozenset({1, 2.3456, "another"})
    x *= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = range(2, 7, 2)')
    print('>>> y = frozenset()')
    print('>>> x *= y')
    print('>>> x')
    x = range(2, 7, 2)
    y = frozenset()
    x *= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = range(2, 7, 2)')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x *= y')
    print('>>> x')
    x = range(2, 7, 2)
    y = frozenset({1, 2.3456, "another"})
    x *= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = range(7, 2, -1)')
    print('>>> y = frozenset()')
    print('>>> x *= y')
    print('>>> x')
    x = range(7, 2, -1)
    y = frozenset()
    x *= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = range(7, 2, -1)')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x *= y')
    print('>>> x')
    x = range(7, 2, -1)
    y = frozenset({1, 2.3456, "another"})
    x *= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = range(7, 2, -2)')
    print('>>> y = frozenset()')
    print('>>> x *= y')
    print('>>> x')
    x = range(7, 2, -2)
    y = frozenset()
    x *= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = range(7, 2, -2)')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x *= y')
    print('>>> x')
    x = range(7, 2, -2)
    y = frozenset({1, 2.3456, "another"})
    x *= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
