try:
    print('>>> x = True')
    print('>>> y = True')
    print('>>> x *= y')
    print('>>> x')
    x = True
    y = True
    x *= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = True')
    print('>>> y = False')
    print('>>> x *= y')
    print('>>> x')
    x = True
    y = False
    x *= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = False')
    print('>>> y = True')
    print('>>> x *= y')
    print('>>> x')
    x = False
    y = True
    x *= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = False')
    print('>>> y = False')
    print('>>> x *= y')
    print('>>> x')
    x = False
    y = False
    x *= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
