try:
    print('>>> f = map')
    print('>>> x = {}')
    print('>>> y = {}')
    print('>>> f(x, y)')
    f = map
    x = {}
    y = {}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = {}')
    print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> f(x, y)')
    f = map
    x = {}
    y = {"a": 1, "c": 2.3456, "d": "another"}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = {}')
    print('>>> f(x, y)')
    f = map
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = {}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> f(x, y)')
    f = map
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = {"a": 1, "c": 2.3456, "d": "another"}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
