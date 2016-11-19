try:
    print('>>> f = property')
    print('>>> x = NotImplemented')
    print('>>> f(x)')
    f = property
    x = NotImplemented
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
