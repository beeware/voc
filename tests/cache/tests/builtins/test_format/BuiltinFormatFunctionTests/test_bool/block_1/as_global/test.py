try:
    print('>>> f = format')
    print('>>> x = True')
    print('>>> f(x)')
    f = format
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = format')
    print('>>> x = False')
    print('>>> f(x)')
    f = format
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
