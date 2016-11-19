try:
    print('>>> f = repr')
    print('>>> x = set()')
    print('>>> f(x)')
    f = repr
    x = set()
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = repr')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> f(x)')
    f = repr
    x = {1, 2.3456, "another"}
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
