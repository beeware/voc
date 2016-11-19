try:
    print('>>> f = isinstance')
    print('>>> x = True')
    print('>>> f(x)')
    f = isinstance
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = isinstance')
    print('>>> x = False')
    print('>>> f(x)')
    f = isinstance
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
