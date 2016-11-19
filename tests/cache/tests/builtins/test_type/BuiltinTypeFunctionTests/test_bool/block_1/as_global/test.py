try:
    print('>>> f = type')
    print('>>> x = True')
    print('>>> f(x)')
    f = type
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = type')
    print('>>> x = False')
    print('>>> f(x)')
    f = type
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
