try:
    print('>>> x = []')
    print('>>> y = None')
    print('>>> x + y')
    x = []
    y = None
    print(x + y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = [3, 4, 5]')
    print('>>> y = None')
    print('>>> x + y')
    x = [3, 4, 5]
    y = None
    print(x + y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
    print('>>> y = None')
    print('>>> x + y')
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = None
    print(x + y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = ["a","b","c"]')
    print('>>> y = None')
    print('>>> x + y')
    x = ["a","b","c"]
    y = None
    print(x + y)
except Exception as e:
    print(type(e), ':', e)
print()
