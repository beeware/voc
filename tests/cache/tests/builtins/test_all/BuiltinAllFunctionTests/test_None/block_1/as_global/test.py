try:
    print('>>> f = all')
    print('>>> x = None')
    print('>>> f(x)')
    f = all
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
