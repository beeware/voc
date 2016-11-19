try:
    print('>>> f = filter')
    print('>>> x = None')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = filter
    x = None
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
