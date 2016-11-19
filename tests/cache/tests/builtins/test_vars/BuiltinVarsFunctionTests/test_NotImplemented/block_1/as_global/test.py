try:
    print('>>> f = vars')
    print('>>> x = NotImplemented')
    print('>>> f(x)')
    f = vars
    x = NotImplemented
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
