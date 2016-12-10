try:
    print('>>> f = pow')
    print('>>> x = None')
    print('>>> f(x)')
    f = pow
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
