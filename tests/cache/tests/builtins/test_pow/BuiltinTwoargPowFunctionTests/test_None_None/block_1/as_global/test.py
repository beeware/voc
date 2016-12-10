try:
    print('>>> f = pow')
    print('>>> x = None')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = pow
    x = None
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
