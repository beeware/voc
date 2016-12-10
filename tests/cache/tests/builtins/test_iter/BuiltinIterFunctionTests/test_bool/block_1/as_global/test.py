try:
    print('>>> f = iter')
    print('>>> x = True')
    print('>>> f(x)')
    f = iter
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = iter')
    print('>>> x = False')
    print('>>> f(x)')
    f = iter
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
