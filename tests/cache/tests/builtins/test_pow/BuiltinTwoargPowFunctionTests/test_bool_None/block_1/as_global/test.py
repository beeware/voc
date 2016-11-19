try:
    print('>>> f = pow')
    print('>>> x = True')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = pow
    x = True
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = False')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = pow
    x = False
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
