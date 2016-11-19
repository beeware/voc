try:
    print('>>> f = hasattr')
    print('>>> x = None')
    print('>>> y = True')
    print('>>> f(x, y)')
    f = hasattr
    x = None
    y = True
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = None')
    print('>>> y = False')
    print('>>> f(x, y)')
    f = hasattr
    x = None
    y = False
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
