try:
    print('>>> x = (1, 2)')
    print('>>> y = True')
    print('>>> x &= y')
    print('>>> x')
    x = (1, 2)
    y = True
    x &= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = (1, 2)')
    print('>>> y = False')
    print('>>> x &= y')
    print('>>> x')
    x = (1, 2)
    y = False
    x &= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
    print('>>> y = True')
    print('>>> x &= y')
    print('>>> x')
    x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    y = True
    x &= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
    print('>>> y = False')
    print('>>> x &= y')
    print('>>> x')
    x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    y = False
    x &= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = (3, 1.2, True, )')
    print('>>> y = True')
    print('>>> x &= y')
    print('>>> x')
    x = (3, 1.2, True, )
    y = True
    x &= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = (3, 1.2, True, )')
    print('>>> y = False')
    print('>>> x &= y')
    print('>>> x')
    x = (3, 1.2, True, )
    y = False
    x &= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = (1, 2.3456, "another")')
    print('>>> y = True')
    print('>>> x &= y')
    print('>>> x')
    x = (1, 2.3456, "another")
    y = True
    x &= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = (1, 2.3456, "another")')
    print('>>> y = False')
    print('>>> x &= y')
    print('>>> x')
    x = (1, 2.3456, "another")
    y = False
    x &= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
