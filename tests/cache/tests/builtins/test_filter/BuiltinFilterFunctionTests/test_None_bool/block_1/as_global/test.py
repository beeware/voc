try:
    print('>>> f = filter')
    print('>>> x = None')
    print('>>> y = True')
    print('>>> f(x, y)')
    f = filter
    x = None
    y = True
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = None')
    print('>>> y = False')
    print('>>> f(x, y)')
    f = filter
    x = None
    y = False
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
