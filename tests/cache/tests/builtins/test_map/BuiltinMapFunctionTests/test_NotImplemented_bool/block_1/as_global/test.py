try:
    print('>>> f = map')
    print('>>> x = NotImplemented')
    print('>>> y = True')
    print('>>> f(x, y)')
    f = map
    x = NotImplemented
    y = True
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = NotImplemented')
    print('>>> y = False')
    print('>>> f(x, y)')
    f = map
    x = NotImplemented
    y = False
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
