try:
    print('>>> f = hasattr')
    print('>>> x = frozenset()')
    print('>>> y = (1, 2)')
    print('>>> f(x, y)')
    f = hasattr
    x = frozenset()
    y = (1, 2)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = frozenset()')
    print('>>> y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
    print('>>> f(x, y)')
    f = hasattr
    x = frozenset()
    y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = frozenset()')
    print('>>> y = (3, 1.2, True, )')
    print('>>> f(x, y)')
    f = hasattr
    x = frozenset()
    y = (3, 1.2, True, )
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = frozenset()')
    print('>>> y = (1, 2.3456, "another")')
    print('>>> f(x, y)')
    f = hasattr
    x = frozenset()
    y = (1, 2.3456, "another")
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = (1, 2)')
    print('>>> f(x, y)')
    f = hasattr
    x = frozenset({1, 2.3456, "another"})
    y = (1, 2)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
    print('>>> f(x, y)')
    f = hasattr
    x = frozenset({1, 2.3456, "another"})
    y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = (3, 1.2, True, )')
    print('>>> f(x, y)')
    f = hasattr
    x = frozenset({1, 2.3456, "another"})
    y = (3, 1.2, True, )
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = (1, 2.3456, "another")')
    print('>>> f(x, y)')
    f = hasattr
    x = frozenset({1, 2.3456, "another"})
    y = (1, 2.3456, "another")
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
