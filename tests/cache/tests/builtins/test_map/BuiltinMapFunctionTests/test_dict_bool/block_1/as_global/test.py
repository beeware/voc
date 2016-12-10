try:
    print('>>> f = map')
    print('>>> x = {}')
    print('>>> y = True')
    print('>>> f(x, y)')
    f = map
    x = {}
    y = True
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = {}')
    print('>>> y = False')
    print('>>> f(x, y)')
    f = map
    x = {}
    y = False
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = True')
    print('>>> f(x, y)')
    f = map
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = True
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = False')
    print('>>> f(x, y)')
    f = map
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = False
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
