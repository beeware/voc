try:
    print('>>> f = object')
    print('>>> x = True')
    print('>>> f(x)')
    f = object
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = object')
    print('>>> x = False')
    print('>>> f(x)')
    f = object
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
