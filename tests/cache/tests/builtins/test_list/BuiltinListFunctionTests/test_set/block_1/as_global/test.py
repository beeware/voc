try:
    print('>>> f = list')
    print('>>> x = set()')
    print('>>> f(x)')
    f = list
    x = set()
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = list')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> f(x)')
    f = list
    x = {1, 2.3456, "another"}
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
