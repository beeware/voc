try:
    print('>>> f = divmod')
    print('>>> x = None')
    print('>>> y = frozenset()')
    print('>>> f(x, y)')
    f = divmod
    x = None
    y = frozenset()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = None')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> f(x, y)')
    f = divmod
    x = None
    y = frozenset({1, 2.3456, "another"})
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
