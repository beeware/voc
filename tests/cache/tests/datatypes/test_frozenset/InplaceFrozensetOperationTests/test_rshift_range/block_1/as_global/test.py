try:
    print('>>> x = frozenset()')
    print('>>> y = range(0)')
    print('>>> x >>= y')
    print('>>> x')
    x = frozenset()
    y = range(0)
    x >>= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset()')
    print('>>> y = range(5)')
    print('>>> x >>= y')
    print('>>> x')
    x = frozenset()
    y = range(5)
    x >>= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset()')
    print('>>> y = range(2, 7)')
    print('>>> x >>= y')
    print('>>> x')
    x = frozenset()
    y = range(2, 7)
    x >>= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset()')
    print('>>> y = range(2, 7, 2)')
    print('>>> x >>= y')
    print('>>> x')
    x = frozenset()
    y = range(2, 7, 2)
    x >>= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset()')
    print('>>> y = range(7, 2, -1)')
    print('>>> x >>= y')
    print('>>> x')
    x = frozenset()
    y = range(7, 2, -1)
    x >>= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset()')
    print('>>> y = range(7, 2, -2)')
    print('>>> x >>= y')
    print('>>> x')
    x = frozenset()
    y = range(7, 2, -2)
    x >>= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = range(0)')
    print('>>> x >>= y')
    print('>>> x')
    x = frozenset({1, 2.3456, "another"})
    y = range(0)
    x >>= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = range(5)')
    print('>>> x >>= y')
    print('>>> x')
    x = frozenset({1, 2.3456, "another"})
    y = range(5)
    x >>= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = range(2, 7)')
    print('>>> x >>= y')
    print('>>> x')
    x = frozenset({1, 2.3456, "another"})
    y = range(2, 7)
    x >>= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = range(2, 7, 2)')
    print('>>> x >>= y')
    print('>>> x')
    x = frozenset({1, 2.3456, "another"})
    y = range(2, 7, 2)
    x >>= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = range(7, 2, -1)')
    print('>>> x >>= y')
    print('>>> x')
    x = frozenset({1, 2.3456, "another"})
    y = range(7, 2, -1)
    x >>= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = range(7, 2, -2)')
    print('>>> x >>= y')
    print('>>> x')
    x = frozenset({1, 2.3456, "another"})
    y = range(7, 2, -2)
    x >>= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
