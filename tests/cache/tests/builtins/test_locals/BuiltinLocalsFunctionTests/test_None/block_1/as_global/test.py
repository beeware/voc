try:
    print('>>> f = locals')
    print('>>> x = None')
    print('>>> f(x)')
    f = locals
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
