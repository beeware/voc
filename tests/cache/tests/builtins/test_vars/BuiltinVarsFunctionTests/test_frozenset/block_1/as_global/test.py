try:
    print('>>> f = vars')
    print('>>> x = frozenset()')
    print('>>> f(x)')
    f = vars
    x = frozenset()
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = vars')
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> f(x)')
    f = vars
    x = frozenset({1, 2.3456, "another"})
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
