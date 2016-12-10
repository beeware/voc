try:
    print('>>> f = callable')
    print('>>> x = True')
    print('>>> f(x)')
    f = callable
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = callable')
    print('>>> x = False')
    print('>>> f(x)')
    f = callable
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
