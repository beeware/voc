try:
    print('>>> f = map')
    print('>>> x = True')
    print('>>> y = set()')
    print('>>> f(x, y)')
    f = map
    x = True
    y = set()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = True')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> f(x, y)')
    f = map
    x = True
    y = {1, 2.3456, "another"}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = False')
    print('>>> y = set()')
    print('>>> f(x, y)')
    f = map
    x = False
    y = set()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = False')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> f(x, y)')
    f = map
    x = False
    y = {1, 2.3456, "another"}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
