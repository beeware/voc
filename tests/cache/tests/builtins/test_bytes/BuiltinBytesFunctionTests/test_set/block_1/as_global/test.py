try:
    print('>>> f = bytes')
    print('>>> x = set()')
    print('>>> f(x)')
    f = bytes
    x = set()
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = bytes')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> f(x)')
    f = bytes
    x = {1, 2.3456, "another"}
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
