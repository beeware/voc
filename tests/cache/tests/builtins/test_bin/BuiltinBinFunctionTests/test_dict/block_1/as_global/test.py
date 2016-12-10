try:
    print('>>> f = bin')
    print('>>> x = {}')
    print('>>> f(x)')
    f = bin
    x = {}
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = bin')
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> f(x)')
    f = bin
    x = {"a": 1, "c": 2.3456, "d": "another"}
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
