try:
    print('>>> x = frozenset()')
    print('>>> y = (1, 2)')
    print('>>> x << y')
    x = frozenset()
    y = (1, 2)
    print(x << y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset()')
    print('>>> y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
    print('>>> x << y')
    x = frozenset()
    y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(x << y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset()')
    print('>>> y = (3, 1.2, True, )')
    print('>>> x << y')
    x = frozenset()
    y = (3, 1.2, True, )
    print(x << y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset()')
    print('>>> y = (1, 2.3456, "another")')
    print('>>> x << y')
    x = frozenset()
    y = (1, 2.3456, "another")
    print(x << y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = (1, 2)')
    print('>>> x << y')
    x = frozenset({1, 2.3456, "another"})
    y = (1, 2)
    print(x << y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
    print('>>> x << y')
    x = frozenset({1, 2.3456, "another"})
    y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(x << y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = (3, 1.2, True, )')
    print('>>> x << y')
    x = frozenset({1, 2.3456, "another"})
    y = (3, 1.2, True, )
    print(x << y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = (1, 2.3456, "another")')
    print('>>> x << y')
    x = frozenset({1, 2.3456, "another"})
    y = (1, 2.3456, "another")
    print(x << y)
except Exception as e:
    print(type(e), ':', e)
print()
