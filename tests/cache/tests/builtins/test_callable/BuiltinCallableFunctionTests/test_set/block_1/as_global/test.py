try:
    print('>>> f = callable')
    print('>>> x = set()')
    print('>>> f(x)')
    f = callable
    x = set()
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = callable')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> f(x)')
    f = callable
    x = {1, 2.3456, "another"}
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
