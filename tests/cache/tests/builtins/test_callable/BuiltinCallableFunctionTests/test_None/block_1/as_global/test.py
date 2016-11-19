try:
    print('>>> f = callable')
    print('>>> x = None')
    print('>>> f(x)')
    f = callable
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
