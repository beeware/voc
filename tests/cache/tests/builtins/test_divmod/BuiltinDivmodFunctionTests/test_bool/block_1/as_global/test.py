try:
    print('>>> f = divmod')
    print('>>> x = True')
    print('>>> f(x)')
    f = divmod
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = False')
    print('>>> f(x)')
    f = divmod
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
