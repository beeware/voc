try:
    print('>>> f = eval')
    print('>>> x = NotImplemented')
    print('>>> f(x)')
    f = eval
    x = NotImplemented
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
