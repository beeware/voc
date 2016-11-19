try:
    print('>>> x = NotImplemented')
    print('>>> y = True')
    print('>>> x ** y')
    x = NotImplemented
    y = True
    print(x ** y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = NotImplemented')
    print('>>> y = False')
    print('>>> x ** y')
    x = NotImplemented
    y = False
    print(x ** y)
except Exception as e:
    print(type(e), ':', e)
print()
