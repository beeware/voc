try:
    print('>>> f = format')
    print('>>> x = set()')
    print('>>> f(x)')
    f = format
    x = set()
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = format')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> f(x)')
    f = format
    x = {1, 2.3456, "another"}
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
