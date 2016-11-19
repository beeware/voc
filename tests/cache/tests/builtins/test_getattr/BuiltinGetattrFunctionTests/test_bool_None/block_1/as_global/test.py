try:
    print('>>> f = getattr')
    print('>>> x = True')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = getattr
    x = True
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = False')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = getattr
    x = False
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
