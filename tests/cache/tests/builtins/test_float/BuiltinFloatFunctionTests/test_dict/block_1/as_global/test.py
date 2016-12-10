try:
    print('>>> f = float')
    print('>>> x = {}')
    print('>>> f(x)')
    f = float
    x = {}
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = float')
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> f(x)')
    f = float
    x = {"a": 1, "c": 2.3456, "d": "another"}
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
