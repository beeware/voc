try:
    print('>>> x = True')
    print('>>> y = slice(0)')
    print('>>> x |= y')
    print('>>> x')
    x = True
    y = slice(0)
    x |= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = True')
    print('>>> y = slice(5)')
    print('>>> x |= y')
    print('>>> x')
    x = True
    y = slice(5)
    x |= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = True')
    print('>>> y = slice(2, 7)')
    print('>>> x |= y')
    print('>>> x')
    x = True
    y = slice(2, 7)
    x |= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = True')
    print('>>> y = slice(2, 7, 2)')
    print('>>> x |= y')
    print('>>> x')
    x = True
    y = slice(2, 7, 2)
    x |= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = True')
    print('>>> y = slice(7, 2, -1)')
    print('>>> x |= y')
    print('>>> x')
    x = True
    y = slice(7, 2, -1)
    x |= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = True')
    print('>>> y = slice(7, 2, -2)')
    print('>>> x |= y')
    print('>>> x')
    x = True
    y = slice(7, 2, -2)
    x |= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = False')
    print('>>> y = slice(0)')
    print('>>> x |= y')
    print('>>> x')
    x = False
    y = slice(0)
    x |= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = False')
    print('>>> y = slice(5)')
    print('>>> x |= y')
    print('>>> x')
    x = False
    y = slice(5)
    x |= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = False')
    print('>>> y = slice(2, 7)')
    print('>>> x |= y')
    print('>>> x')
    x = False
    y = slice(2, 7)
    x |= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = False')
    print('>>> y = slice(2, 7, 2)')
    print('>>> x |= y')
    print('>>> x')
    x = False
    y = slice(2, 7, 2)
    x |= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = False')
    print('>>> y = slice(7, 2, -1)')
    print('>>> x |= y')
    print('>>> x')
    x = False
    y = slice(7, 2, -1)
    x |= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = False')
    print('>>> y = slice(7, 2, -2)')
    print('>>> x |= y')
    print('>>> x')
    x = False
    y = slice(7, 2, -2)
    x |= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
