try:
    print('>>> f = divmod')
    print('>>> x = None')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = divmod
    x = None
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
