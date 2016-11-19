try:
    print('>>> f = iter')
    print('>>> x = None')
    print('>>> f(x)')
    f = iter
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
