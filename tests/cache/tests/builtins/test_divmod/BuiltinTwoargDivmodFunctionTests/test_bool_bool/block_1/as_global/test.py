try:
    print('>>> f = divmod')
    print('>>> x = True')
    print('>>> y = True')
    print('>>> f(x, y)')
    f = divmod
    x = True
    y = True
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = True')
    print('>>> y = False')
    print('>>> f(x, y)')
    f = divmod
    x = True
    y = False
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = False')
    print('>>> y = True')
    print('>>> f(x, y)')
    f = divmod
    x = False
    y = True
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = False')
    print('>>> y = False')
    print('>>> f(x, y)')
    f = divmod
    x = False
    y = False
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
