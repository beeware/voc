try:
    print('>>> f = __import__')
    print('>>> x = []')
    print('>>> f(x)')
    f = __import__
    x = []
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = __import__')
    print('>>> x = [3, 4, 5]')
    print('>>> f(x)')
    f = __import__
    x = [3, 4, 5]
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = __import__')
    print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
    print('>>> f(x)')
    f = __import__
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = __import__')
    print('>>> x = ["a","b","c"]')
    print('>>> f(x)')
    f = __import__
    x = ["a","b","c"]
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
