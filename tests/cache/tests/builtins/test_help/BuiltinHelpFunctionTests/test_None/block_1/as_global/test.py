try:
    print('>>> f = help')
    print('>>> x = None')
    print('>>> f(x)')
    f = help
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
