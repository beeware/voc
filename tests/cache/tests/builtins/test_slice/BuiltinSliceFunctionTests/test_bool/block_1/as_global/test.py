try:
    print('>>> f = slice')
    print('>>> x = True')
    print('>>> f(x)')
    f = slice
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = slice')
    print('>>> x = False')
    print('>>> f(x)')
    f = slice
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
