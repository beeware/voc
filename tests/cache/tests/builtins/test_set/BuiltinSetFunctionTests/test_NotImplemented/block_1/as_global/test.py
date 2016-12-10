try:
    print('>>> f = set')
    print('>>> x = NotImplemented')
    print('>>> f(x)')
    f = set
    x = NotImplemented
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
