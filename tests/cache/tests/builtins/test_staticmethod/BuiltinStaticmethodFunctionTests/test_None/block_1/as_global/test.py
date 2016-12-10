try:
    print('>>> f = staticmethod')
    print('>>> x = None')
    print('>>> f(x)')
    f = staticmethod
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
