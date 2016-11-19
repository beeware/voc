try:
    print('>>> f = hasattr')
    print('>>> x = NotImplemented')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = hasattr
    x = NotImplemented
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
