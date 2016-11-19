try:
    print('>>> f = tuple')
    print('>>> x = None')
    print('>>> f(x)')
    f = tuple
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
