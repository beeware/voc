try:
    print('>>> x = slice(0)')
    print('>>> not x')
    x = slice(0)
    print(not x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(5)')
    print('>>> not x')
    x = slice(5)
    print(not x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(2, 7)')
    print('>>> not x')
    x = slice(2, 7)
    print(not x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(2, 7, 2)')
    print('>>> not x')
    x = slice(2, 7, 2)
    print(not x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(7, 2, -1)')
    print('>>> not x')
    x = slice(7, 2, -1)
    print(not x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(7, 2, -2)')
    print('>>> not x')
    x = slice(7, 2, -2)
    print(not x)
except Exception as e:
    print(type(e), ':', e)
print()
