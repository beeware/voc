try:
    print('>>> f = frozenset')
    print('>>> x = NotImplemented')
    print('>>> f(x)')
    f = frozenset
    x = NotImplemented
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
