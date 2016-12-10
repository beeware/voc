try:
    print('>>> f = abs')
    print('>>> x = NotImplemented')
    print('>>> f(x)')
    f = abs
    x = NotImplemented
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
