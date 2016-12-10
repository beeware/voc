try:
    print('>>> f = ascii')
    print('>>> x = None')
    print('>>> f(x)')
    f = ascii
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
