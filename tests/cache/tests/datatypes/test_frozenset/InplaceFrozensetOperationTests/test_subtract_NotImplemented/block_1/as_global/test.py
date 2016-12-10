try:
    print('>>> x = frozenset()')
    print('>>> y = NotImplemented')
    print('>>> x -= y')
    print('>>> x')
    x = frozenset()
    y = NotImplemented
    x -= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = NotImplemented')
    print('>>> x -= y')
    print('>>> x')
    x = frozenset({1, 2.3456, "another"})
    y = NotImplemented
    x -= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
