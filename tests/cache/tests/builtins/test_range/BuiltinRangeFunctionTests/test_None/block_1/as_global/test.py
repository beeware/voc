try:
    print('>>> f = range')
    print('>>> x = None')
    print('>>> f(x)')
    f = range
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
