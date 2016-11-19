try:
    print('>>> f = divmod')
    print('>>> x = True')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = divmod
    x = True
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = False')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = divmod
    x = False
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
