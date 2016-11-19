try:
    print('>>> x = NotImplemented')
    print('>>> y = NotImplemented')
    print('>>> x >> y')
    x = NotImplemented
    y = NotImplemented
    print(x >> y)
except Exception as e:
    print(type(e), ':', e)
print()
