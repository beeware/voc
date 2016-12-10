try:
    print('>>> f = pow')
    print('>>> x = 1j')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = pow
    x = 1j
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = 3.14159265j')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = pow
    x = 3.14159265j
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = 1+2j')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = pow
    x = 1+2j
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = 3-4j')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = pow
    x = 3-4j
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = -5j')
    print('>>> y = None')
    print('>>> f(x, y)')
    f = pow
    x = -5j
    y = None
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
