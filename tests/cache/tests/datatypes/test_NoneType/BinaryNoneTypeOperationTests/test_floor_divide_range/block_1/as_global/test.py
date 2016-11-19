try:
    print('>>> x = None')
    print('>>> y = range(0)')
    print('>>> x // y')
    x = None
    y = range(0)
    print(x // y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = None')
    print('>>> y = range(5)')
    print('>>> x // y')
    x = None
    y = range(5)
    print(x // y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = None')
    print('>>> y = range(2, 7)')
    print('>>> x // y')
    x = None
    y = range(2, 7)
    print(x // y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = None')
    print('>>> y = range(2, 7, 2)')
    print('>>> x // y')
    x = None
    y = range(2, 7, 2)
    print(x // y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = None')
    print('>>> y = range(7, 2, -1)')
    print('>>> x // y')
    x = None
    y = range(7, 2, -1)
    print(x // y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = None')
    print('>>> y = range(7, 2, -2)')
    print('>>> x // y')
    x = None
    y = range(7, 2, -2)
    print(x // y)
except Exception as e:
    print(type(e), ':', e)
print()
