try:
    print('>>> f = map')
    print('>>> x = NotImplemented')
    print('>>> y = set()')
    print('>>> f(x, y)')
    f = map
    x = NotImplemented
    y = set()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = NotImplemented')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> f(x, y)')
    f = map
    x = NotImplemented
    y = {1, 2.3456, "another"}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
