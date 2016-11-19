try:
    print('>>> f = exec')
    print('>>> x = True')
    print('>>> f(x)')
    f = exec
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = exec')
    print('>>> x = False')
    print('>>> f(x)')
    f = exec
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
