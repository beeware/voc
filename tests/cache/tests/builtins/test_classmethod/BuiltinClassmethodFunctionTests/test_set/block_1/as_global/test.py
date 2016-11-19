try:
    print('>>> f = classmethod')
    print('>>> x = set()')
    print('>>> f(x)')
    f = classmethod
    x = set()
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = classmethod')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> f(x)')
    f = classmethod
    x = {1, 2.3456, "another"}
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
