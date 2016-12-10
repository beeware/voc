try:
    print('>>> f = all')
    print('>>> x = True')
    print('>>> f(x)')
    f = all
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = all')
    print('>>> x = False')
    print('>>> f(x)')
    f = all
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
