try:
    print('>>> f = bool')
    print('>>> x = None')
    print('>>> f(x)')
    f = bool
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
