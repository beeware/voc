try:
    print('>>> f = chr')
    print('>>> x = NotImplemented')
    print('>>> f(x)')
    f = chr
    x = NotImplemented
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
