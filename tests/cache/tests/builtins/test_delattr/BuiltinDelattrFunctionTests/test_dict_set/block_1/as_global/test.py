try:
    print('>>> f = delattr')
    print('>>> x = {}')
    print('>>> y = set()')
    print('>>> f(x, y)')
    f = delattr
    x = {}
    y = set()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = delattr')
    print('>>> x = {}')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> f(x, y)')
    f = delattr
    x = {}
    y = {1, 2.3456, "another"}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = delattr')
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = set()')
    print('>>> f(x, y)')
    f = delattr
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = set()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = delattr')
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> f(x, y)')
    f = delattr
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = {1, 2.3456, "another"}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
