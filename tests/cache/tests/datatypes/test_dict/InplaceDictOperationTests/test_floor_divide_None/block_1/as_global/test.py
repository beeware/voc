try:
    print('>>> x = {}')
    print('>>> y = None')
    print('>>> x //= y')
    print('>>> x')
    x = {}
    y = None
    x //= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = None')
    print('>>> x //= y')
    print('>>> x')
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = None
    x //= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
