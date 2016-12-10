try:
    print('>>> f = id')
    print('>>> x = None')
    print('>>> f(x)')
    f = id
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
