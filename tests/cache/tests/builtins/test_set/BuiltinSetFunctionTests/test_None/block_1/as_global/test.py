try:
    print('>>> f = set')
    print('>>> x = None')
    print('>>> f(x)')
    f = set
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
