try:
    print('>>> f = float')
    print('>>> x = None')
    print('>>> f(x)')
    f = float
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
