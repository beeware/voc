try:
    print('>>> f = range')
    print('>>> x = set()')
    print('>>> f(x)')
    f = range
    x = set()
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = range')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> f(x)')
    f = range
    x = {1, 2.3456, "another"}
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
