try:
    print('>>> x = {}')
    print('>>> y = NotImplemented')
    print('>>> x ^= y')
    print('>>> x')
    x = {}
    y = NotImplemented
    x ^= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = NotImplemented')
    print('>>> x ^= y')
    print('>>> x')
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = NotImplemented
    x ^= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
