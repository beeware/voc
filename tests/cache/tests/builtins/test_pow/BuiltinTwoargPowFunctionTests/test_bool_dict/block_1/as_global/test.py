try:
    print('>>> f = pow')
    print('>>> x = True')
    print('>>> y = {}')
    print('>>> f(x, y)')
    f = pow
    x = True
    y = {}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = True')
    print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> f(x, y)')
    f = pow
    x = True
    y = {"a": 1, "c": 2.3456, "d": "another"}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = False')
    print('>>> y = {}')
    print('>>> f(x, y)')
    f = pow
    x = False
    y = {}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = False')
    print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> f(x, y)')
    f = pow
    x = False
    y = {"a": 1, "c": 2.3456, "d": "another"}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
