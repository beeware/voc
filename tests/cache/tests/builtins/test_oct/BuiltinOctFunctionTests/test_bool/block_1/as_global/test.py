try:
    print('>>> f = oct')
    print('>>> x = True')
    print('>>> f(x)')
    f = oct
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = oct')
    print('>>> x = False')
    print('>>> f(x)')
    f = oct
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
