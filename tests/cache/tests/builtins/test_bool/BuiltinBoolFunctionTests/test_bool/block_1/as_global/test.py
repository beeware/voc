try:
    print('>>> f = bool')
    print('>>> x = True')
    print('>>> f(x)')
    f = bool
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = bool')
    print('>>> x = False')
    print('>>> f(x)')
    f = bool
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
