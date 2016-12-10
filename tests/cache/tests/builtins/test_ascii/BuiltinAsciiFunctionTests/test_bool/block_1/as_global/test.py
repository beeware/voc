try:
    print('>>> f = ascii')
    print('>>> x = True')
    print('>>> f(x)')
    f = ascii
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = ascii')
    print('>>> x = False')
    print('>>> f(x)')
    f = ascii
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
