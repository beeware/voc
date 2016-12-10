try:
    print('>>> f = list')
    print('>>> x = True')
    print('>>> f(x)')
    f = list
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = list')
    print('>>> x = False')
    print('>>> f(x)')
    f = list
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
