try:
    print('>>> x = None')
    print('>>> not x')
    x = None
    print(not x)
except Exception as e:
    print(type(e), ':', e)
print()
