try:
    print('>>> f = hasattr')
    print('>>> x = {}')
    print('>>> y = True')
    print('>>> f(x, y)')
    f = hasattr
    x = {}
    y = True
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = {}')
    print('>>> y = False')
    print('>>> f(x, y)')
    f = hasattr
    x = {}
    y = False
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = True')
    print('>>> f(x, y)')
    f = hasattr
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = True
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = False')
    print('>>> f(x, y)')
    f = hasattr
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = False
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
