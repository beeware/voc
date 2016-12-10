try:
    print('>>> f = bytes')
    print('>>> x = NotImplemented')
    print('>>> f(x)')
    f = bytes
    x = NotImplemented
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
