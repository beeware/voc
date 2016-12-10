try:
    print('>>> f = set')
    print('>>> x = range(0)')
    print('>>> f(x)')
    f = set
    x = range(0)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = set')
    print('>>> x = range(5)')
    print('>>> f(x)')
    f = set
    x = range(5)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = set')
    print('>>> x = range(2, 7)')
    print('>>> f(x)')
    f = set
    x = range(2, 7)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = set')
    print('>>> x = range(2, 7, 2)')
    print('>>> f(x)')
    f = set
    x = range(2, 7, 2)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = set')
    print('>>> x = range(7, 2, -1)')
    print('>>> f(x)')
    f = set
    x = range(7, 2, -1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = set')
    print('>>> x = range(7, 2, -2)')
    print('>>> f(x)')
    f = set
    x = range(7, 2, -2)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
