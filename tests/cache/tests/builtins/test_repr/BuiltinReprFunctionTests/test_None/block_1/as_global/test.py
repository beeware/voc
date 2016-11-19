try:
    print('>>> f = repr')
    print('>>> x = None')
    print('>>> f(x)')
    f = repr
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
