try:
    print('>>> f = getattr')
    print('>>> x = None')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = getattr
    x = None
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
