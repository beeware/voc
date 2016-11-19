try:
    print('>>> f = map')
    print('>>> x = NotImplemented')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = map
    x = NotImplemented
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
