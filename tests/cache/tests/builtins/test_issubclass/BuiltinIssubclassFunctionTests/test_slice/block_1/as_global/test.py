try:
    print('>>> f = issubclass')
    print('>>> x = slice(0)')
    print('>>> f(x)')
    f = issubclass
    x = slice(0)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = issubclass')
    print('>>> x = slice(5)')
    print('>>> f(x)')
    f = issubclass
    x = slice(5)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = issubclass')
    print('>>> x = slice(2, 7)')
    print('>>> f(x)')
    f = issubclass
    x = slice(2, 7)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = issubclass')
    print('>>> x = slice(2, 7, 2)')
    print('>>> f(x)')
    f = issubclass
    x = slice(2, 7, 2)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = issubclass')
    print('>>> x = slice(7, 2, -1)')
    print('>>> f(x)')
    f = issubclass
    x = slice(7, 2, -1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = issubclass')
    print('>>> x = slice(7, 2, -2)')
    print('>>> f(x)')
    f = issubclass
    x = slice(7, 2, -2)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
