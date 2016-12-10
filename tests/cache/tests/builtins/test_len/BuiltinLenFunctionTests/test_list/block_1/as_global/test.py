try:
    print('>>> f = len')
    print('>>> x = []')
    print('>>> f(x)')
    f = len
    x = []
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = len')
    print('>>> x = [3, 4, 5]')
    print('>>> f(x)')
    f = len
    x = [3, 4, 5]
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = len')
    print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
    print('>>> f(x)')
    f = len
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = len')
    print('>>> x = ["a","b","c"]')
    print('>>> f(x)')
    f = len
    x = ["a","b","c"]
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
