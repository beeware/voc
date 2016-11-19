try:
    print('>>> x = range(0)')
    print('>>> y = None')
    print('>>> x += y')
    print('>>> x')
    x = range(0)
    y = None
    x += y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = range(5)')
    print('>>> y = None')
    print('>>> x += y')
    print('>>> x')
    x = range(5)
    y = None
    x += y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = range(2, 7)')
    print('>>> y = None')
    print('>>> x += y')
    print('>>> x')
    x = range(2, 7)
    y = None
    x += y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = range(2, 7, 2)')
    print('>>> y = None')
    print('>>> x += y')
    print('>>> x')
    x = range(2, 7, 2)
    y = None
    x += y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = range(7, 2, -1)')
    print('>>> y = None')
    print('>>> x += y')
    print('>>> x')
    x = range(7, 2, -1)
    y = None
    x += y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = range(7, 2, -2)')
    print('>>> y = None')
    print('>>> x += y')
    print('>>> x')
    x = range(7, 2, -2)
    y = None
    x += y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
