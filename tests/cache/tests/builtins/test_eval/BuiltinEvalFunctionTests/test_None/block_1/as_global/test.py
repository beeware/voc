try:
    print('>>> f = eval')
    print('>>> x = None')
    print('>>> f(x)')
    f = eval
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
