try:
    print('>>> f = ascii')
    print('>>> x = {}')
    print('>>> f(x)')
    f = ascii
    x = {}
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = ascii')
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> f(x)')
    f = ascii
    x = {"a": 1, "c": 2.3456, "d": "another"}
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
