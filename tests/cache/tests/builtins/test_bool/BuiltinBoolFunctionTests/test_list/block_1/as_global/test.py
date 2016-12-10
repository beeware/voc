try:
    print('>>> f = bool')
    print('>>> x = []')
    print('>>> f(x)')
    f = bool
    x = []
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = bool')
    print('>>> x = [3, 4, 5]')
    print('>>> f(x)')
    f = bool
    x = [3, 4, 5]
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = bool')
    print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
    print('>>> f(x)')
    f = bool
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = bool')
    print('>>> x = ["a","b","c"]')
    print('>>> f(x)')
    f = bool
    x = ["a","b","c"]
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
