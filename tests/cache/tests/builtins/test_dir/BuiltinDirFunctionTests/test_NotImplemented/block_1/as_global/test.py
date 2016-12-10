try:
    print('>>> f = dir')
    print('>>> x = NotImplemented')
    print('>>> f(x)')
    f = dir
    x = NotImplemented
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
