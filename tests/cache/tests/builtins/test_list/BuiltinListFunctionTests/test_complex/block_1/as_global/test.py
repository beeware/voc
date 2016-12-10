try:
    print('>>> f = list')
    print('>>> x = 1j')
    print('>>> f(x)')
    f = list
    x = 1j
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = list')
    print('>>> x = 3.14159265j')
    print('>>> f(x)')
    f = list
    x = 3.14159265j
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = list')
    print('>>> x = 1+2j')
    print('>>> f(x)')
    f = list
    x = 1+2j
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = list')
    print('>>> x = 3-4j')
    print('>>> f(x)')
    f = list
    x = 3-4j
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = list')
    print('>>> x = -5j')
    print('>>> f(x)')
    f = list
    x = -5j
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
