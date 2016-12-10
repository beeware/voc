try:
    print('>>> f = map')
    print('>>> x = (1, 2)')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = map
    x = (1, 2)
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = map
    x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = (3, 1.2, True, )')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = map
    x = (3, 1.2, True, )
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = (1, 2.3456, "another")')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = map
    x = (1, 2.3456, "another")
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
