try:
    print('>>> f = frozenset')
    print('>>> x = True')
    print('>>> f(x)')
    f = frozenset
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = frozenset')
    print('>>> x = False')
    print('>>> f(x)')
    f = frozenset
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
