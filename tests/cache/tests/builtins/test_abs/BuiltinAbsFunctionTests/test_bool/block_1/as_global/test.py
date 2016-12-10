try:
    print('>>> f = abs')
    print('>>> x = True')
    print('>>> f(x)')
    f = abs
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = abs')
    print('>>> x = False')
    print('>>> f(x)')
    f = abs
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
