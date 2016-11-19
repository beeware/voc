try:
    print('>>> f = sorted')
    print('>>> x = None')
    print('>>> f(x)')
    f = sorted
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
