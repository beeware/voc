try:
    print('>>> f = getattr')
    print('>>> x = None')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = getattr
    x = None
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
