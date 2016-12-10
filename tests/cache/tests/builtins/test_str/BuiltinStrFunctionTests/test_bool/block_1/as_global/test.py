try:
    print('>>> f = str')
    print('>>> x = True')
    print('>>> f(x)')
    f = str
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = str')
    print('>>> x = False')
    print('>>> f(x)')
    f = str
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
