try:
    print('>>> f = filter')
    print('>>> x = None')
    print('>>> y = []')
    print('>>> f(x, y)')
    f = filter
    x = None
    y = []
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = None')
    print('>>> y = [3, 4, 5]')
    print('>>> f(x, y)')
    f = filter
    x = None
    y = [3, 4, 5]
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = None')
    print('>>> y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
    print('>>> f(x, y)')
    f = filter
    x = None
    y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = filter')
    print('>>> x = None')
    print('>>> y = ["a","b","c"]')
    print('>>> f(x, y)')
    f = filter
    x = None
    y = ["a","b","c"]
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
