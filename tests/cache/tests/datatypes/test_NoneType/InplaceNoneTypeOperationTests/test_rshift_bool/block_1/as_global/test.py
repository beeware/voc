try:
    print('>>> x = None')
    print('>>> y = True')
    print('>>> x >>= y')
    print('>>> x')
    x = None
    y = True
    x >>= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = None')
    print('>>> y = False')
    print('>>> x >>= y')
    print('>>> x')
    x = None
    y = False
    x >>= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
