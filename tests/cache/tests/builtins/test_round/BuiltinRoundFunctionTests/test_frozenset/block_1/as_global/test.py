try:
    print('>>> f = round')
    print('>>> x = frozenset()')
    print('>>> f(x)')
    f = round
    x = frozenset()
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = round')
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> f(x)')
    f = round
    x = frozenset({1, 2.3456, "another"})
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
