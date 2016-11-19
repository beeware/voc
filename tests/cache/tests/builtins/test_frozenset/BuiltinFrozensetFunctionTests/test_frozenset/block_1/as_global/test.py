try:
    print('>>> f = frozenset')
    print('>>> x = frozenset()')
    print('>>> f(x)')
    f = frozenset
    x = frozenset()
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = frozenset')
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> f(x)')
    f = frozenset
    x = frozenset({1, 2.3456, "another"})
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
