try:
    print('>>> f = hasattr')
    print('>>> x = True')
    print('>>> y = True')
    print('>>> f(x, y)')
    f = hasattr
    x = True
    y = True
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = True')
    print('>>> y = False')
    print('>>> f(x, y)')
    f = hasattr
    x = True
    y = False
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = False')
    print('>>> y = True')
    print('>>> f(x, y)')
    f = hasattr
    x = False
    y = True
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = False')
    print('>>> y = False')
    print('>>> f(x, y)')
    f = hasattr
    x = False
    y = False
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
