try:
    print('>>> f = ascii')
    print('>>> x = slice(0)')
    print('>>> f(x)')
    f = ascii
    x = slice(0)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = ascii')
    print('>>> x = slice(5)')
    print('>>> f(x)')
    f = ascii
    x = slice(5)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = ascii')
    print('>>> x = slice(2, 7)')
    print('>>> f(x)')
    f = ascii
    x = slice(2, 7)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = ascii')
    print('>>> x = slice(2, 7, 2)')
    print('>>> f(x)')
    f = ascii
    x = slice(2, 7, 2)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = ascii')
    print('>>> x = slice(7, 2, -1)')
    print('>>> f(x)')
    f = ascii
    x = slice(7, 2, -1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = ascii')
    print('>>> x = slice(7, 2, -2)')
    print('>>> f(x)')
    f = ascii
    x = slice(7, 2, -2)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
