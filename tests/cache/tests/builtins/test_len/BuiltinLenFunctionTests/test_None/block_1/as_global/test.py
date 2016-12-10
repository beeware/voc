try:
    print('>>> f = len')
    print('>>> x = None')
    print('>>> f(x)')
    f = len
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
