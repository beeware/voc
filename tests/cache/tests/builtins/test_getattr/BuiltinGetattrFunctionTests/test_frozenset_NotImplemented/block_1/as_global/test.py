try:
    print('>>> f = getattr')
    print('>>> x = frozenset()')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = getattr
    x = frozenset()
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = getattr
    x = frozenset({1, 2.3456, "another"})
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
