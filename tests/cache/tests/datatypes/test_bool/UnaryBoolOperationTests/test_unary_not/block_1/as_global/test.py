try:
    print('>>> x = True')
    print('>>> not x')
    x = True
    print(not x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = False')
    print('>>> not x')
    x = False
    print(not x)
except Exception as e:
    print(type(e), ':', e)
print()
