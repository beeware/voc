try:
    print('>>> f = vars')
    print('>>> x = set()')
    print('>>> f(x)')
    f = vars
    x = set()
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = vars')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> f(x)')
    f = vars
    x = {1, 2.3456, "another"}
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
