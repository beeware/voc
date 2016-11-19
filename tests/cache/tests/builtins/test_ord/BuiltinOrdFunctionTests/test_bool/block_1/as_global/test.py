try:
    print('>>> f = ord')
    print('>>> x = True')
    print('>>> f(x)')
    f = ord
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = ord')
    print('>>> x = False')
    print('>>> f(x)')
    f = ord
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
