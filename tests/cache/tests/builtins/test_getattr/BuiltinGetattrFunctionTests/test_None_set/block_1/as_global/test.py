try:
    print('>>> f = getattr')
    print('>>> x = None')
    print('>>> y = set()')
    print('>>> f(x, y)')
    f = getattr
    x = None
    y = set()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = None')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> f(x, y)')
    f = getattr
    x = None
    y = {1, 2.3456, "another"}
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
