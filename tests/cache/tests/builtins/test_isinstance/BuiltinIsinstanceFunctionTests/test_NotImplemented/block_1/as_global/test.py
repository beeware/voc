try:
    print('>>> f = isinstance')
    print('>>> x = NotImplemented')
    print('>>> f(x)')
    f = isinstance
    x = NotImplemented
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
