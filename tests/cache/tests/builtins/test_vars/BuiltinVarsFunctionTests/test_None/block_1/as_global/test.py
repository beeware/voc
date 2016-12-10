try:
    print('>>> f = vars')
    print('>>> x = None')
    print('>>> f(x)')
    f = vars
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
