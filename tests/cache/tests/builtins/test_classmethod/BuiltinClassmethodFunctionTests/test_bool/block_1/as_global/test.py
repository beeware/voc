try:
    print('>>> f = classmethod')
    print('>>> x = True')
    print('>>> f(x)')
    f = classmethod
    x = True
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = classmethod')
    print('>>> x = False')
    print('>>> f(x)')
    f = classmethod
    x = False
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
