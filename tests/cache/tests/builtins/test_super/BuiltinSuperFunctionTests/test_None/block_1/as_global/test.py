try:
    print('>>> f = super')
    print('>>> x = None')
    print('>>> f(x)')
    f = super
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
