try:
    print('>>> f = pow')
    print('>>> x = {}')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = pow
    x = {}
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = NotImplemented')
    print('>>> f(x, y)')
    f = pow
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = NotImplemented
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
