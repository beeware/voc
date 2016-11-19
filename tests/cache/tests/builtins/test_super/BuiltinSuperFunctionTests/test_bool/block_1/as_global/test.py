try:
    print('>>> f = super')
    print('>>> x = True')
    print('>>> f(x)')
    f = super
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = super')
    print('>>> x = False')
    print('>>> f(x)')
    f = super
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
