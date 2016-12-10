try:
    print('>>> f = map')
    print('>>> x = None')
    print('>>> y = True')
    print('>>> f(x, y)')
    f = map
    x = None
    y = True
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = None')
    print('>>> y = False')
    print('>>> f(x, y)')
    f = map
    x = None
    y = False
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
