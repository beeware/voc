try:
    print('>>> f = enumerate')
    print('>>> x = True')
    print('>>> f(x)')
    f = enumerate
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = enumerate')
    print('>>> x = False')
    print('>>> f(x)')
    f = enumerate
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
