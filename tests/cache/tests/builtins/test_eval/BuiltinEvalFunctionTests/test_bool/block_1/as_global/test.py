try:
    print('>>> f = eval')
    print('>>> x = True')
    print('>>> f(x)')
    f = eval
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = eval')
    print('>>> x = False')
    print('>>> f(x)')
    f = eval
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
