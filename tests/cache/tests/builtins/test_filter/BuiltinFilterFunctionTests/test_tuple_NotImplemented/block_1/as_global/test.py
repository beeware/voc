try:
    print('>>> f = filter')
    print('>>> x = (1, 2)')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = filter
    x = (1, 2)
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = filter
    x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = (3, 1.2, True, )')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = filter
    x = (3, 1.2, True, )
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = (1, 2.3456, "another")')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = filter
    x = (1, 2.3456, "another")
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
