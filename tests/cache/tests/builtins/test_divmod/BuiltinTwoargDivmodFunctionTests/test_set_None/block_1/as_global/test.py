try:
    print('>>> f = divmod')
    print('>>> x = set()')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = divmod
    x = set()
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = divmod
    x = {1, 2.3456, "another"}
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
