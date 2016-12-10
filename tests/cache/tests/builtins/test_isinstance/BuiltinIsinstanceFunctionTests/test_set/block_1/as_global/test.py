try:
    print('>>> f = isinstance')
    print('>>> x = set()')
    print('>>> f(x)')
    f = isinstance
    x = set()
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = isinstance')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> f(x)')
    f = isinstance
    x = {1, 2.3456, "another"}
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
