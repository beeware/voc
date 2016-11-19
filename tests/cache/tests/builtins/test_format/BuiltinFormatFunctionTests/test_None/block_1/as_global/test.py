try:
    print('>>> f = format')
    print('>>> x = None')
    print('>>> f(x)')
    f = format
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
