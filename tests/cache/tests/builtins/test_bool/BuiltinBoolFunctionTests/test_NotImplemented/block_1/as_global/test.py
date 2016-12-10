try:
    print('>>> f = bool')
    print('>>> x = NotImplemented')
    print('>>> f(x)')
    f = bool
    x = NotImplemented
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
