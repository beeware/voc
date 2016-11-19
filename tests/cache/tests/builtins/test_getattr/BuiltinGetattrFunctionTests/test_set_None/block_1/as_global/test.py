try:
    print('>>> f = getattr')
    print('>>> x = set()')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = getattr
    x = set()
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = getattr')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = getattr
    x = {1, 2.3456, "another"}
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
