try:
    print('>>> x = NotImplemented')
    print('>>> y = {}')
    print('>>> x /= y')
    print('>>> x')
    x = NotImplemented
    y = {}
    x /= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = NotImplemented')
    print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> x /= y')
    print('>>> x')
    x = NotImplemented
    y = {"a": 1, "c": 2.3456, "d": "another"}
    x /= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
