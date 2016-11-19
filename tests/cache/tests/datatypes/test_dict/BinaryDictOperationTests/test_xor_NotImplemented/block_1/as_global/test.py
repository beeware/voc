try:
    print('>>> x = {}')
    print('>>> y = NotImplemented')
    print('>>> x ^ y')
    x = {}
    y = NotImplemented
    print(x ^ y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = NotImplemented')
    print('>>> x ^ y')
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = NotImplemented
    print(x ^ y)
except Exception as e:
    print(type(e), ':', e)
print()
