try:
    print('>>> f = slice')
    print('>>> x = None')
    print('>>> f(x)')
    f = slice
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
