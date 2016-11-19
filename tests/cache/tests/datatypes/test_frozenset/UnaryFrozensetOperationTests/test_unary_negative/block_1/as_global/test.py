try:
    print('>>> x = frozenset()')
    print('>>> -x')
    x = frozenset()
    print(-x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> -x')
    x = frozenset({1, 2.3456, "another"})
    print(-x)
except Exception as e:
    print(type(e), ':', e)
print()
