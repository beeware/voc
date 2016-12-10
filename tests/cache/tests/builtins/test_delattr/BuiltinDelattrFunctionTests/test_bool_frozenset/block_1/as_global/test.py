try:
    print('>>> f = delattr')
    print('>>> x = True')
    print('>>> y = frozenset()')
    print('>>> f(x, y)')
    f = delattr
    x = True
    y = frozenset()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = delattr')
    print('>>> x = True')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> f(x, y)')
    f = delattr
    x = True
    y = frozenset({1, 2.3456, "another"})
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = delattr')
    print('>>> x = False')
    print('>>> y = frozenset()')
    print('>>> f(x, y)')
    f = delattr
    x = False
    y = frozenset()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = delattr')
    print('>>> x = False')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> f(x, y)')
    f = delattr
    x = False
    y = frozenset({1, 2.3456, "another"})
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
