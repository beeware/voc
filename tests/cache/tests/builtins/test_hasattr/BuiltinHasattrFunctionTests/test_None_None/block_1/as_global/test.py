try:
    print('>>> f = hasattr')
    print('>>> x = None')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = hasattr
    x = None
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
