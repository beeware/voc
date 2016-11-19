try:
    print('>>> f = ord')
    print('>>> x = NotImplemented')
    print('>>> f(x)')
    f = ord
    x = NotImplemented
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
