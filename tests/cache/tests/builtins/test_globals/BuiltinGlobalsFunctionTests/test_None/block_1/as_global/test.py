try:
    print('>>> f = globals')
    print('>>> x = None')
    print('>>> f(x)')
    f = globals
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
