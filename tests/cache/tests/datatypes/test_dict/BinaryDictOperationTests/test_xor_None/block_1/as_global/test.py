try:
    print('>>> x = {}')
    print('>>> y = None')
    print('>>> x ^ y')
    x = {}
    y = None
    print(x ^ y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = None')
    print('>>> x ^ y')
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = None
    print(x ^ y)
except Exception as e:
    print(type(e), ':', e)
print()
