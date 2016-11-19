try:
    print('>>> f = set')
    print('>>> x = True')
    print('>>> f(x)')
    f = set
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = set')
    print('>>> x = False')
    print('>>> f(x)')
    f = set
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
