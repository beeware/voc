try:
    print('>>> f = locals')
    print('>>> x = 3')
    print('>>> f(x)')
    f = locals
    x = 3
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = locals')
    print('>>> x = 0')
    print('>>> f(x)')
    f = locals
    x = 0
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = locals')
    print('>>> x = -5')
    print('>>> f(x)')
    f = locals
    x = -5
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = locals')
    print('>>> x = -3')
    print('>>> f(x)')
    f = locals
    x = -3
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = locals')
    print('>>> x = 5')
    print('>>> f(x)')
    f = locals
    x = 5
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = locals')
    print('>>> x = 1')
    print('>>> f(x)')
    f = locals
    x = 1
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
