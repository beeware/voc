try:
    print('>>> f = range')
    print('>>> x = True')
    print('>>> f(x)')
    f = range
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = range')
    print('>>> x = False')
    print('>>> f(x)')
    f = range
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
