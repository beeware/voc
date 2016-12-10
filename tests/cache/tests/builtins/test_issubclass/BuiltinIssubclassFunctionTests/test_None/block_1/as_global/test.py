try:
    print('>>> f = issubclass')
    print('>>> x = None')
    print('>>> f(x)')
    f = issubclass
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
