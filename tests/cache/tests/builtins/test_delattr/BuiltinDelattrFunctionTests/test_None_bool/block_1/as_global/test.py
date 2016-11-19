try:
    print('>>> f = delattr')
    print('>>> x = None')
    print('>>> y = True')
    print('>>> f(x, y)')
    f = delattr
    x = None
    y = True
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = delattr')
    print('>>> x = None')
    print('>>> y = False')
    print('>>> f(x, y)')
    f = delattr
    x = None
    y = False
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
