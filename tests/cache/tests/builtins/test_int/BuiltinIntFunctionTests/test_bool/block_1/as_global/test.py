try:
    print('>>> f = int')
    print('>>> x = True')
    print('>>> f(x)')
    f = int
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = int')
    print('>>> x = False')
    print('>>> f(x)')
    f = int
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
