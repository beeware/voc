try:
    print('>>> f = open')
    print('>>> x = None')
    print('>>> f(x)')
    f = open
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
