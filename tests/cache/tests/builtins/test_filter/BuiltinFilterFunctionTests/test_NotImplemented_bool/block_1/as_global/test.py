try:
    print('>>> f = filter')
    print('>>> x = NotImplemented')
    print('>>> y = True')
    print('>>> f(x, y)')
    f = filter
    x = NotImplemented
    y = True
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = NotImplemented')
    print('>>> y = False')
    print('>>> f(x, y)')
    f = filter
    x = NotImplemented
    y = False
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
