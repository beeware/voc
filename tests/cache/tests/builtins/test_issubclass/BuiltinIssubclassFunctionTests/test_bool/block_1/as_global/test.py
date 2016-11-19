try:
    print('>>> f = issubclass')
    print('>>> x = True')
    print('>>> f(x)')
    f = issubclass
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = issubclass')
    print('>>> x = False')
    print('>>> f(x)')
    f = issubclass
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
