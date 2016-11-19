try:
    print('>>> x = range(0)')
    print('>>> not x')
    x = range(0)
    print(not x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = range(5)')
    print('>>> not x')
    x = range(5)
    print(not x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = range(2, 7)')
    print('>>> not x')
    x = range(2, 7)
    print(not x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = range(2, 7, 2)')
    print('>>> not x')
    x = range(2, 7, 2)
    print(not x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = range(7, 2, -1)')
    print('>>> not x')
    x = range(7, 2, -1)
    print(not x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = range(7, 2, -2)')
    print('>>> not x')
    x = range(7, 2, -2)
    print(not x)
except Exception as e:
    print(type(e), ':', e)
print()
