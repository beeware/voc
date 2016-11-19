try:
    print('>>> f = divmod')
    print('>>> x = {}')
    print('>>> y = {}')
    print('>>> f(x, y)')
    f = divmod
    x = {}
    y = {}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = {}')
    print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> f(x, y)')
    f = divmod
    x = {}
    y = {"a": 1, "c": 2.3456, "d": "another"}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = {}')
    print('>>> f(x, y)')
    f = divmod
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = {}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> f(x, y)')
    f = divmod
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = {"a": 1, "c": 2.3456, "d": "another"}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
