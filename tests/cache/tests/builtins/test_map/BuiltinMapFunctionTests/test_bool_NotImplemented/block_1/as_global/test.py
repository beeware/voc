try:
    print('>>> f = map')
    print('>>> x = True')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = map
    x = True
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = False')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = map
    x = False
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
