try:
    print('>>> f = pow')
    print('>>> x = NotImplemented')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = pow
    x = NotImplemented
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
