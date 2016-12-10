try:
    print('>>> x = True')
    print('>>> y = None')
    print('>>> x | y')
    x = True
    y = None
    print(x | y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = False')
    print('>>> y = None')
    print('>>> x | y')
    x = False
    y = None
    print(x | y)
except Exception as e:
    print(type(e), ':', e)
print()
