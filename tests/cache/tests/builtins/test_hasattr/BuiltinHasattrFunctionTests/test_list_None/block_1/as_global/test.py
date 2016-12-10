try:
    print('>>> f = hasattr')
    print('>>> x = []')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = hasattr
    x = []
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = [3, 4, 5]')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = hasattr
    x = [3, 4, 5]
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = hasattr
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hasattr')
    print('>>> x = ["a","b","c"]')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = hasattr
    x = ["a","b","c"]
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
