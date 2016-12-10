try:
    print('>>> f = list')
    print('>>> x = NotImplemented')
    print('>>> f(x)')
    f = list
    x = NotImplemented
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
