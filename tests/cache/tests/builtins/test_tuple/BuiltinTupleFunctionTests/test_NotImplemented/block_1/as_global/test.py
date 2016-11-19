try:
    print('>>> f = tuple')
    print('>>> x = NotImplemented')
    print('>>> f(x)')
    f = tuple
    x = NotImplemented
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
