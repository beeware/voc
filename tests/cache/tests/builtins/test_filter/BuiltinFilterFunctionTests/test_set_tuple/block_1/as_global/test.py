try:
    print('>>> f = filter')
    print('>>> x = set()')
    print('>>> y = (1, 2)')
    print('>>> f(x, y)')
    f = filter
    x = set()
    y = (1, 2)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = set()')
    print('>>> y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
    print('>>> f(x, y)')
    f = filter
    x = set()
    y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = set()')
    print('>>> y = (3, 1.2, True, )')
    print('>>> f(x, y)')
    f = filter
    x = set()
    y = (3, 1.2, True, )
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = set()')
    print('>>> y = (1, 2.3456, "another")')
    print('>>> f(x, y)')
    f = filter
    x = set()
    y = (1, 2.3456, "another")
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = (1, 2)')
    print('>>> f(x, y)')
    f = filter
    x = {1, 2.3456, "another"}
    y = (1, 2)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
    print('>>> f(x, y)')
    f = filter
    x = {1, 2.3456, "another"}
    y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = (3, 1.2, True, )')
    print('>>> f(x, y)')
    f = filter
    x = {1, 2.3456, "another"}
    y = (3, 1.2, True, )
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = (1, 2.3456, "another")')
    print('>>> f(x, y)')
    f = filter
    x = {1, 2.3456, "another"}
    y = (1, 2.3456, "another")
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
