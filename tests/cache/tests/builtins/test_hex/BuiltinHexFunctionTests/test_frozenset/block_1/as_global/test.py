try:
    print('>>> f = hex')
    print('>>> x = frozenset()')
    print('>>> f(x)')
    f = hex
    x = frozenset()
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hex')
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> f(x)')
    f = hex
    x = frozenset({1, 2.3456, "another"})
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
