try:
    print('>>> x = slice(0)')
    print('>>> y = True')
    print('>>> x + y')
    x = slice(0)
    y = True
    print(x + y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(0)')
    print('>>> y = False')
    print('>>> x + y')
    x = slice(0)
    y = False
    print(x + y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(5)')
    print('>>> y = True')
    print('>>> x + y')
    x = slice(5)
    y = True
    print(x + y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(5)')
    print('>>> y = False')
    print('>>> x + y')
    x = slice(5)
    y = False
    print(x + y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(2, 7)')
    print('>>> y = True')
    print('>>> x + y')
    x = slice(2, 7)
    y = True
    print(x + y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(2, 7)')
    print('>>> y = False')
    print('>>> x + y')
    x = slice(2, 7)
    y = False
    print(x + y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(2, 7, 2)')
    print('>>> y = True')
    print('>>> x + y')
    x = slice(2, 7, 2)
    y = True
    print(x + y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(2, 7, 2)')
    print('>>> y = False')
    print('>>> x + y')
    x = slice(2, 7, 2)
    y = False
    print(x + y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(7, 2, -1)')
    print('>>> y = True')
    print('>>> x + y')
    x = slice(7, 2, -1)
    y = True
    print(x + y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(7, 2, -1)')
    print('>>> y = False')
    print('>>> x + y')
    x = slice(7, 2, -1)
    y = False
    print(x + y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(7, 2, -2)')
    print('>>> y = True')
    print('>>> x + y')
    x = slice(7, 2, -2)
    y = True
    print(x + y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(7, 2, -2)')
    print('>>> y = False')
    print('>>> x + y')
    x = slice(7, 2, -2)
    y = False
    print(x + y)
except Exception as e:
    print(type(e), ':', e)
print()
