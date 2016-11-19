try:
    print('>>> f = id')
    print('>>> x = True')
    print('>>> f(x)')
    f = id
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = id')
    print('>>> x = False')
    print('>>> f(x)')
    f = id
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
