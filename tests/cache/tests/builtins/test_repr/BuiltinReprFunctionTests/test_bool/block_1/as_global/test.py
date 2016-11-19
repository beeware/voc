try:
    print('>>> f = repr')
    print('>>> x = True')
    print('>>> f(x)')
    f = repr
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = repr')
    print('>>> x = False')
    print('>>> f(x)')
    f = repr
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
