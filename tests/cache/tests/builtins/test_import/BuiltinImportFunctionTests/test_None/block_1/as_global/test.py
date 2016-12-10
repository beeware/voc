try:
    print('>>> f = __import__')
    print('>>> x = None')
    print('>>> f(x)')
    f = __import__
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
