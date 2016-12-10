try:
    print('>>> f = filter')
    print('>>> x = NotImplemented')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = filter
    x = NotImplemented
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
