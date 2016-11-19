try:
    print('>>> f = sorted')
    print('>>> x = NotImplemented')
    print('>>> f(x)')
    f = sorted
    x = NotImplemented
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
