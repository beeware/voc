try:
    print('>>> f = len')
    print('>>> x = 1j')
    print('>>> f(x)')
    f = len
    x = 1j
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = len')
    print('>>> x = 3.14159265j')
    print('>>> f(x)')
    f = len
    x = 3.14159265j
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = len')
    print('>>> x = 1+2j')
    print('>>> f(x)')
    f = len
    x = 1+2j
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = len')
    print('>>> x = 3-4j')
    print('>>> f(x)')
    f = len
    x = 3-4j
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = len')
    print('>>> x = -5j')
    print('>>> f(x)')
    f = len
    x = -5j
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
