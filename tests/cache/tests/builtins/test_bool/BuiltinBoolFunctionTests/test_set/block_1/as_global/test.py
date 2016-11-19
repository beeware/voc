try:
    print('>>> f = bool')
    print('>>> x = set()')
    print('>>> f(x)')
    f = bool
    x = set()
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = bool')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> f(x)')
    f = bool
    x = {1, 2.3456, "another"}
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
