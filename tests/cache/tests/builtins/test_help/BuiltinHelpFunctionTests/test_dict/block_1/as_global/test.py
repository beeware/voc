try:
    print('>>> f = help')
    print('>>> x = {}')
    print('>>> f(x)')
    f = help
    x = {}
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = help')
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> f(x)')
    f = help
    x = {"a": 1, "c": 2.3456, "d": "another"}
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
