try:
    print('>>> f = compile')
    print('>>> x = True')
    print('>>> f(x)')
    f = compile
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = compile')
    print('>>> x = False')
    print('>>> f(x)')
    f = compile
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
