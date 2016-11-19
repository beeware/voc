try:
    print('>>> f = memoryview')
    print('>>> x = None')
    print('>>> f(x)')
    f = memoryview
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
