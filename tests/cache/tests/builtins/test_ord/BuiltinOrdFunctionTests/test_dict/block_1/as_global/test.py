try:
    print('>>> f = ord')
    print('>>> x = {}')
    print('>>> f(x)')
    f = ord
    x = {}
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = ord')
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> f(x)')
    f = ord
    x = {"a": 1, "c": 2.3456, "d": "another"}
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
