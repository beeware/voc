try:
    print('>>> x = []')
    print('>>> y = None')
    print('>>> x <<= y')
    print('>>> x')
    x = []
    y = None
    x <<= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = [3, 4, 5]')
    print('>>> y = None')
    print('>>> x <<= y')
    print('>>> x')
    x = [3, 4, 5]
    y = None
    x <<= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
    print('>>> y = None')
    print('>>> x <<= y')
    print('>>> x')
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = None
    x <<= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = ["a","b","c"]')
    print('>>> y = None')
    print('>>> x <<= y')
    print('>>> x')
    x = ["a","b","c"]
    y = None
    x <<= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
