try:
    print('>>> f = pow')
    print('>>> x = True')
    print('>>> y = set()')
    print('>>> f(x, y)')
    f = pow
    x = True
    y = set()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = True')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> f(x, y)')
    f = pow
    x = True
    y = {1, 2.3456, "another"}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = False')
    print('>>> y = set()')
    print('>>> f(x, y)')
    f = pow
    x = False
    y = set()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = False')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> f(x, y)')
    f = pow
    x = False
    y = {1, 2.3456, "another"}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
