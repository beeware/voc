try:
    print('>>> f = bytes')
    print('>>> x = slice(0)')
    print('>>> f(x)')
    f = bytes
    x = slice(0)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = bytes')
    print('>>> x = slice(5)')
    print('>>> f(x)')
    f = bytes
    x = slice(5)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = bytes')
    print('>>> x = slice(2, 7)')
    print('>>> f(x)')
    f = bytes
    x = slice(2, 7)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = bytes')
    print('>>> x = slice(2, 7, 2)')
    print('>>> f(x)')
    f = bytes
    x = slice(2, 7, 2)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = bytes')
    print('>>> x = slice(7, 2, -1)')
    print('>>> f(x)')
    f = bytes
    x = slice(7, 2, -1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = bytes')
    print('>>> x = slice(7, 2, -2)')
    print('>>> f(x)')
    f = bytes
    x = slice(7, 2, -2)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
