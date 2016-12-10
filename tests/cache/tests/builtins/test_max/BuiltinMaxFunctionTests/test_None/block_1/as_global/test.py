try:
    print('>>> f = max')
    print('>>> x = None')
    print('>>> f(x)')
    f = max
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
