try:
    print('>>> f = float')
    print('>>> x = NotImplemented')
    print('>>> f(x)')
    f = float
    x = NotImplemented
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
