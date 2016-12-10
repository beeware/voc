try:
    print('>>> f = dir')
    print('>>> x = set()')
    print('>>> f(x)')
    f = dir
    x = set()
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = dir')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> f(x)')
    f = dir
    x = {1, 2.3456, "another"}
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
