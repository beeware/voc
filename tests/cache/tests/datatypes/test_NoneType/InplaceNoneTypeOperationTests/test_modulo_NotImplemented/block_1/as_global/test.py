try:
    print('>>> x = None')
    print('>>> y = NotImplemented')
    print('>>> x %= y')
    print('>>> x')
    x = None
    y = NotImplemented
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
