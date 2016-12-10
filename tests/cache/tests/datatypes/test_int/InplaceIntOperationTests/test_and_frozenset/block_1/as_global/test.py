try:
    print('>>> x = 3')
    print('>>> y = frozenset()')
    print('>>> x &= y')
    print('>>> x')
    x = 3
    y = frozenset()
    x &= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = 3')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x &= y')
    print('>>> x')
    x = 3
    y = frozenset({1, 2.3456, "another"})
    x &= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = 0')
    print('>>> y = frozenset()')
    print('>>> x &= y')
    print('>>> x')
    x = 0
    y = frozenset()
    x &= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = 0')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x &= y')
    print('>>> x')
    x = 0
    y = frozenset({1, 2.3456, "another"})
    x &= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = -5')
    print('>>> y = frozenset()')
    print('>>> x &= y')
    print('>>> x')
    x = -5
    y = frozenset()
    x &= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = -5')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x &= y')
    print('>>> x')
    x = -5
    y = frozenset({1, 2.3456, "another"})
    x &= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = -3')
    print('>>> y = frozenset()')
    print('>>> x &= y')
    print('>>> x')
    x = -3
    y = frozenset()
    x &= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = -3')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x &= y')
    print('>>> x')
    x = -3
    y = frozenset({1, 2.3456, "another"})
    x &= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = 5')
    print('>>> y = frozenset()')
    print('>>> x &= y')
    print('>>> x')
    x = 5
    y = frozenset()
    x &= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = 5')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x &= y')
    print('>>> x')
    x = 5
    y = frozenset({1, 2.3456, "another"})
    x &= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = 1')
    print('>>> y = frozenset()')
    print('>>> x &= y')
    print('>>> x')
    x = 1
    y = frozenset()
    x &= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = 1')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x &= y')
    print('>>> x')
    x = 1
    y = frozenset({1, 2.3456, "another"})
    x &= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
