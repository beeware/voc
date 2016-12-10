try:
    print('>>> x = NotImplemented')
    print('>>> y = None')
    print('>>> x -= y')
    print('>>> x')
    x = NotImplemented
    y = None
    x -= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
