try:
    print('>>> f = memoryview')
    print('>>> x = NotImplemented')
    print('>>> f(x)')
    f = memoryview
    x = NotImplemented
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
