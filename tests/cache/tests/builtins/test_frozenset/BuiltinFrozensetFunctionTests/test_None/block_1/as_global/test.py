try:
    print('>>> f = frozenset')
    print('>>> x = None')
    print('>>> f(x)')
    f = frozenset
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
