try:
    print('>>> f = dir')
    print('>>> x = True')
    print('>>> f(x)')
    f = dir
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = dir')
    print('>>> x = False')
    print('>>> f(x)')
    f = dir
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
