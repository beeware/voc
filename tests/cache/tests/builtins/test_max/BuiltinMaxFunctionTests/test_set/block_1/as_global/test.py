try:
    print('>>> f = max')
    print('>>> x = set()')
    print('>>> f(x)')
    f = max
    x = set()
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = max')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> f(x)')
    f = max
    x = {1, 2.3456, "another"}
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
