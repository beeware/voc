try:
    print('>>> f = vars')
    print('>>> x = True')
    print('>>> f(x)')
    f = vars
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = vars')
    print('>>> x = False')
    print('>>> f(x)')
    f = vars
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
