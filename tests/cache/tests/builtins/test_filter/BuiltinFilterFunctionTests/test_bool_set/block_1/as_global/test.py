try:
    print('>>> f = filter')
    print('>>> x = True')
    print('>>> y = set()')
    print('>>> f(x, y)')
    f = filter
    x = True
    y = set()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = True')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> f(x, y)')
    f = filter
    x = True
    y = {1, 2.3456, "another"}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = False')
    print('>>> y = set()')
    print('>>> f(x, y)')
    f = filter
    x = False
    y = set()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = False')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> f(x, y)')
    f = filter
    x = False
    y = {1, 2.3456, "another"}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
