try:
    print('>>> f = getattr')
    print('>>> x = True')
    print('>>> y = True')
    print('>>> f(x, y)')
    f = getattr
    x = True
    y = True
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = True')
    print('>>> y = False')
    print('>>> f(x, y)')
    f = getattr
    x = True
    y = False
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = False')
    print('>>> y = True')
    print('>>> f(x, y)')
    f = getattr
    x = False
    y = True
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = False')
    print('>>> y = False')
    print('>>> f(x, y)')
    f = getattr
    x = False
    y = False
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
