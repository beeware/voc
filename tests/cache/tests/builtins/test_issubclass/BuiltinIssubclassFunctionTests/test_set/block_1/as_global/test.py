try:
    print('>>> f = issubclass')
    print('>>> x = set()')
    print('>>> f(x)')
    f = issubclass
    x = set()
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = issubclass')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> f(x)')
    f = issubclass
    x = {1, 2.3456, "another"}
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
