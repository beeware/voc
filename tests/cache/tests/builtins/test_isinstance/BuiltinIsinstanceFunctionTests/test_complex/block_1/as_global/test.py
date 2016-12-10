try:
    print('>>> f = isinstance')
    print('>>> x = 1j')
    print('>>> f(x)')
    f = isinstance
    x = 1j
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = isinstance')
    print('>>> x = 3.14159265j')
    print('>>> f(x)')
    f = isinstance
    x = 3.14159265j
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = isinstance')
    print('>>> x = 1+2j')
    print('>>> f(x)')
    f = isinstance
    x = 1+2j
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = isinstance')
    print('>>> x = 3-4j')
    print('>>> f(x)')
    f = isinstance
    x = 3-4j
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = isinstance')
    print('>>> x = -5j')
    print('>>> f(x)')
    f = isinstance
    x = -5j
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
