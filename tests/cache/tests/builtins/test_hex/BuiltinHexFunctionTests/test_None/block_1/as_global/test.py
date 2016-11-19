try:
    print('>>> f = hex')
    print('>>> x = None')
    print('>>> f(x)')
    f = hex
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
