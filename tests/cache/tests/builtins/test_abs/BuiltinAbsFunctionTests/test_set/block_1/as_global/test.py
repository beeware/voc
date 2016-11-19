try:
    print('>>> f = abs')
    print('>>> x = set()')
    print('>>> f(x)')
    f = abs
    x = set()
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = abs')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> f(x)')
    f = abs
    x = {1, 2.3456, "another"}
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
