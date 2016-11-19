try:
    print('>>> x = NotImplemented')
    print('>>> y = []')
    print('>>> x << y')
    x = NotImplemented
    y = []
    print(x << y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = NotImplemented')
    print('>>> y = [3, 4, 5]')
    print('>>> x << y')
    x = NotImplemented
    y = [3, 4, 5]
    print(x << y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = NotImplemented')
    print('>>> y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
    print('>>> x << y')
    x = NotImplemented
    y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(x << y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = NotImplemented')
    print('>>> y = ["a","b","c"]')
    print('>>> x << y')
    x = NotImplemented
    y = ["a","b","c"]
    print(x << y)
except Exception as e:
    print(type(e), ':', e)
print()
