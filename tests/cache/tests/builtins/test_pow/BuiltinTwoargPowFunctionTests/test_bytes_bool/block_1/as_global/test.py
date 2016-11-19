try:
    print('>>> f = pow')
    print('>>> x = b""')
    print('>>> y = True')
    print('>>> f(x, y)')
    f = pow
    x = b""
    y = True
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = b""')
    print('>>> y = False')
    print('>>> f(x, y)')
    f = pow
    x = b""
    y = False
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = b"This is another string of bytes"')
    print('>>> y = True')
    print('>>> f(x, y)')
    f = pow
    x = b"This is another string of bytes"
    y = True
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = b"This is another string of bytes"')
    print('>>> y = False')
    print('>>> f(x, y)')
    f = pow
    x = b"This is another string of bytes"
    y = False
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
