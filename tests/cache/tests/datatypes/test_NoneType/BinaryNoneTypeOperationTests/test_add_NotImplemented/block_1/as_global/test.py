try:
    print('>>> x = None')
    print('>>> y = NotImplemented')
    print('>>> x + y')
    x = None
    y = NotImplemented
    print(x + y)
except Exception as e:
    print(type(e), ':', e)
print()
