try:
    print('>>> x = None')
    print('>>> y = 1j')
    print('>>> x ** y')
    x = None
    y = 1j
    print(x ** y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = None')
    print('>>> y = 3.14159265j')
    print('>>> x ** y')
    x = None
    y = 3.14159265j
    print(x ** y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = None')
    print('>>> y = 1+2j')
    print('>>> x ** y')
    x = None
    y = 1+2j
    print(x ** y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = None')
    print('>>> y = 3-4j')
    print('>>> x ** y')
    x = None
    y = 3-4j
    print(x ** y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = None')
    print('>>> y = -5j')
    print('>>> x ** y')
    x = None
    y = -5j
    print(x ** y)
except Exception as e:
    print(type(e), ':', e)
print()
