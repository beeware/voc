try:
    print('>>> f = type')
    print('>>> x = None')
    print('>>> f(x)')
    f = type
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
