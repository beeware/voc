try:
    print('>>> f = dict')
    print('>>> x = True')
    print('>>> f(x)')
    f = dict
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = dict')
    print('>>> x = False')
    print('>>> f(x)')
    f = dict
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
