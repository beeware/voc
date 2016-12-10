try:
    print('>>> f = delattr')
    print('>>> x = (1, 2)')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = delattr
    x = (1, 2)
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = delattr')
    print('>>> x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = delattr
    x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = delattr')
    print('>>> x = (3, 1.2, True, )')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = delattr
    x = (3, 1.2, True, )
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = delattr')
    print('>>> x = (1, 2.3456, "another")')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = delattr
    x = (1, 2.3456, "another")
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
