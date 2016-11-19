try:
    print('>>> f = abs')
    print('>>> x = None')
    print('>>> f(x)')
    f = abs
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
