try:
    print('>>> f = hasattr')
    print('>>> x = None')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = hasattr
    x = None
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
