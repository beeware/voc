try:
    print('>>> x = NotImplemented')
    print('>>> y = frozenset()')
    print('>>> x << y')
    x = NotImplemented
    y = frozenset()
    print(x << y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = NotImplemented')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x << y')
    x = NotImplemented
    y = frozenset({1, 2.3456, "another"})
    print(x << y)
except Exception as e:
    print(type(e), ':', e)
print()
