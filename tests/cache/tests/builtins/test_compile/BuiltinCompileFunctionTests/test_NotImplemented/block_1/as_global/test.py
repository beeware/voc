try:
    print('>>> f = compile')
    print('>>> x = NotImplemented')
    print('>>> f(x)')
    f = compile
    x = NotImplemented
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
