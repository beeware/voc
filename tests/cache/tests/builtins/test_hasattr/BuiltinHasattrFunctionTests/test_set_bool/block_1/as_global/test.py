try:
    print('>>> f = hasattr')
    print('>>> x = set()')
    print('>>> y = True')
    print('>>> f(x, y)')
    f = hasattr
    x = set()
    y = True
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = set()')
    print('>>> y = False')
    print('>>> f(x, y)')
    f = hasattr
    x = set()
    y = False
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = True')
    print('>>> f(x, y)')
    f = hasattr
    x = {1, 2.3456, "another"}
    y = True
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = False')
    print('>>> f(x, y)')
    f = hasattr
    x = {1, 2.3456, "another"}
    y = False
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
