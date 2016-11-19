try:
    print('>>> f = bin')
    print('>>> x = NotImplemented')
    print('>>> f(x)')
    f = bin
    x = NotImplemented
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
