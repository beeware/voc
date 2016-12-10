try:
    print('>>> f = type')
    print('>>> x = NotImplemented')
    print('>>> f(x)')
    f = type
    x = NotImplemented
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
