try:
    print('>>> f = ord')
    print('>>> x = None')
    print('>>> f(x)')
    f = ord
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
