try:
    print('>>> f = exec')
    print('>>> x = []')
    print('>>> f(x)')
    f = exec
    x = []
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = exec')
    print('>>> x = [3, 4, 5]')
    print('>>> f(x)')
    f = exec
    x = [3, 4, 5]
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = exec')
    print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
    print('>>> f(x)')
    f = exec
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = exec')
    print('>>> x = ["a","b","c"]')
    print('>>> f(x)')
    f = exec
    x = ["a","b","c"]
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
