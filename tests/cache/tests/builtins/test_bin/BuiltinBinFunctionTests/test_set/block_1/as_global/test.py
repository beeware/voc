try:
    print('>>> f = bin')
    print('>>> x = set()')
    print('>>> f(x)')
    f = bin
    x = set()
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = bin')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> f(x)')
    f = bin
    x = {1, 2.3456, "another"}
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
