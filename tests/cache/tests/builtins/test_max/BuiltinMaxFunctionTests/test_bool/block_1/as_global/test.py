try:
    print('>>> f = max')
    print('>>> x = True')
    print('>>> f(x)')
    f = max
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = max')
    print('>>> x = False')
    print('>>> f(x)')
    f = max
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
