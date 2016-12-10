try:
    print('>>> f = locals')
    print('>>> x = []')
    print('>>> f(x)')
    f = locals
    x = []
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = locals')
    print('>>> x = [3, 4, 5]')
    print('>>> f(x)')
    f = locals
    x = [3, 4, 5]
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = locals')
    print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
    print('>>> f(x)')
    f = locals
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = locals')
    print('>>> x = ["a","b","c"]')
    print('>>> f(x)')
    f = locals
    x = ["a","b","c"]
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
