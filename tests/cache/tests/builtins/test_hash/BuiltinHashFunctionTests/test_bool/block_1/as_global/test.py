try:
    print('>>> f = hash')
    print('>>> x = True')
    print('>>> f(x)')
    f = hash
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hash')
    print('>>> x = False')
    print('>>> f(x)')
    f = hash
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
