try:
    print('>>> f = any')
    print('>>> x = True')
    print('>>> f(x)')
    f = any
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = any')
    print('>>> x = False')
    print('>>> f(x)')
    f = any
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
