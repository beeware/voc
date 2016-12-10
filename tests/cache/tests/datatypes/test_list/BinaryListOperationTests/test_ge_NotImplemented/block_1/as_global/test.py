try:
    print('>>> x = []')
    print('>>> y = NotImplemented')
    print('>>> x >= y')
    x = []
    y = NotImplemented
    print(x >= y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = [3, 4, 5]')
    print('>>> y = NotImplemented')
    print('>>> x >= y')
    x = [3, 4, 5]
    y = NotImplemented
    print(x >= y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
    print('>>> y = NotImplemented')
    print('>>> x >= y')
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = NotImplemented
    print(x >= y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = ["a","b","c"]')
    print('>>> y = NotImplemented')
    print('>>> x >= y')
    x = ["a","b","c"]
    y = NotImplemented
    print(x >= y)
except Exception as e:
    print(type(e), ':', e)
print()
