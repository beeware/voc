try:
    print('>>> f = help')
    print('>>> x = NotImplemented')
    print('>>> f(x)')
    f = help
    x = NotImplemented
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
