try:
    print('>>> f = map')
    print('>>> x = None')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = map
    x = None
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
