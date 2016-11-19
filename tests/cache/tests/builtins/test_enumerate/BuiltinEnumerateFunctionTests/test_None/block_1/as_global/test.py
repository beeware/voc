try:
    print('>>> f = enumerate')
    print('>>> x = None')
    print('>>> f(x)')
    f = enumerate
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
