try:
    print('>>> x = None')
    print('>>> -x')
    x = None
    print(-x)
except Exception as e:
    print(type(e), ':', e)
print()
