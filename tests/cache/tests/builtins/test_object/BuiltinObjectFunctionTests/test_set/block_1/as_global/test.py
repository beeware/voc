try:
    print('>>> f = object')
    print('>>> x = set()')
    print('>>> f(x)')
    f = object
    x = set()
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = object')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> f(x)')
    f = object
    x = {1, 2.3456, "another"}
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
