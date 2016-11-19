try:
    print('>>> f = tuple')
    print('>>> x = True')
    print('>>> f(x)')
    f = tuple
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = tuple')
    print('>>> x = False')
    print('>>> f(x)')
    f = tuple
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
