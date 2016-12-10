try:
    print('>>> x = None')
    print('>>> y = []')
    print('>>> x /= y')
    print('>>> x')
    x = None
    y = []
    x /= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = None')
    print('>>> y = [3, 4, 5]')
    print('>>> x /= y')
    print('>>> x')
    x = None
    y = [3, 4, 5]
    x /= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = None')
    print('>>> y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
    print('>>> x /= y')
    print('>>> x')
    x = None
    y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    x /= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = None')
    print('>>> y = ["a","b","c"]')
    print('>>> x /= y')
    print('>>> x')
    x = None
    y = ["a","b","c"]
    x /= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
