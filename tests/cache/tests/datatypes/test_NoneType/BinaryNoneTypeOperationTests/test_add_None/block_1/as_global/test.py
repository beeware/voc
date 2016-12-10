try:
    print('>>> x = None')
    print('>>> y = None')
    print('>>> x + y')
    x = None
    y = None
    print(x + y)
except Exception as e:
    print(type(e), ':', e)
print()
