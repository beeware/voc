try:
    print('>>> x = frozenset()')
    print('>>> y = None')
    print('>>> x //= y')
    print('>>> x')
    x = frozenset()
    y = None
    x //= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = None')
    print('>>> x //= y')
    print('>>> x')
    x = frozenset({1, 2.3456, "another"})
    y = None
    x //= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
