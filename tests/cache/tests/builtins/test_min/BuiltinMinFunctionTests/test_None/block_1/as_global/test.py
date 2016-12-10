try:
    print('>>> f = min')
    print('>>> x = None')
    print('>>> f(x)')
    f = min
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
