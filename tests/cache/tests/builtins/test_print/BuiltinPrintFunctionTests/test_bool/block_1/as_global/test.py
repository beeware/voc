try:
    print('>>> f = print')
    print('>>> x = True')
    print('>>> f(x)')
    f = print
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = print')
    print('>>> x = False')
    print('>>> f(x)')
    f = print
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
