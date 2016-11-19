try:
    print('>>> f = hasattr')
    print('>>> x = NotImplemented')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = hasattr
    x = NotImplemented
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
