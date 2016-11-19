try:
    print('>>> f = next')
    print('>>> x = slice(0)')
    print('>>> f(x)')
    f = next
    x = slice(0)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = next')
    print('>>> x = slice(5)')
    print('>>> f(x)')
    f = next
    x = slice(5)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = next')
    print('>>> x = slice(2, 7)')
    print('>>> f(x)')
    f = next
    x = slice(2, 7)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = next')
    print('>>> x = slice(2, 7, 2)')
    print('>>> f(x)')
    f = next
    x = slice(2, 7, 2)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = next')
    print('>>> x = slice(7, 2, -1)')
    print('>>> f(x)')
    f = next
    x = slice(7, 2, -1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = next')
    print('>>> x = slice(7, 2, -2)')
    print('>>> f(x)')
    f = next
    x = slice(7, 2, -2)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
