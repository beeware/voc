try:
    print('>>> f = float')
    print('>>> x = set()')
    print('>>> f(x)')
    f = float
    x = set()
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = float')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> f(x)')
    f = float
    x = {1, 2.3456, "another"}
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
