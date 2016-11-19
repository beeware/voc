try:
    print('>>> f = round')
    print('>>> x = None')
    print('>>> f(x)')
    f = round
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
