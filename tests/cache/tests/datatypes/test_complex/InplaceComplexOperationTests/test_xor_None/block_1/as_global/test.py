try:
    print('>>> x = 1j')
    print('>>> y = None')
    print('>>> x ^= y')
    print('>>> x')
    x = 1j
    y = None
    x ^= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = 3.14159265j')
    print('>>> y = None')
    print('>>> x ^= y')
    print('>>> x')
    x = 3.14159265j
    y = None
    x ^= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = 1+2j')
    print('>>> y = None')
    print('>>> x ^= y')
    print('>>> x')
    x = 1+2j
    y = None
    x ^= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = 3-4j')
    print('>>> y = None')
    print('>>> x ^= y')
    print('>>> x')
    x = 3-4j
    y = None
    x ^= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = -5j')
    print('>>> y = None')
    print('>>> x ^= y')
    print('>>> x')
    x = -5j
    y = None
    x ^= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
