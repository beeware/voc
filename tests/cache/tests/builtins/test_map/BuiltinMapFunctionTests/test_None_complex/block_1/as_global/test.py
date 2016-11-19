try:
    print('>>> f = map')
    print('>>> x = None')
    print('>>> y = 1j')
    print('>>> f(x, y)')
    f = map
    x = None
    y = 1j
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = None')
    print('>>> y = 3.14159265j')
    print('>>> f(x, y)')
    f = map
    x = None
    y = 3.14159265j
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = None')
    print('>>> y = 1+2j')
    print('>>> f(x, y)')
    f = map
    x = None
    y = 1+2j
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = None')
    print('>>> y = 3-4j')
    print('>>> f(x, y)')
    f = map
    x = None
    y = 3-4j
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = None')
    print('>>> y = -5j')
    print('>>> f(x, y)')
    f = map
    x = None
    y = -5j
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
