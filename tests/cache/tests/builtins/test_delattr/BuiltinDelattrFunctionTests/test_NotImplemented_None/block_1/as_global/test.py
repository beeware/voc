try:
    print('>>> f = delattr')
    print('>>> x = NotImplemented')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = delattr
    x = NotImplemented
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
