try:
    print('>>> f = dir')
    print('>>> x = None')
    print('>>> f(x)')
    f = dir
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
