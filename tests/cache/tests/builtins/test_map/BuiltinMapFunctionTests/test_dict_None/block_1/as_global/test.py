try:
    print('>>> f = map')
    print('>>> x = {}')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = map
    x = {}
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = map
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
