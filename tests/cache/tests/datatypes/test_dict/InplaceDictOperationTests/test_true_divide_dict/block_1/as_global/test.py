try:
    print('>>> x = {}')
    print('>>> y = {}')
    print('>>> x /= y')
    print('>>> x')
    x = {}
    y = {}
    x /= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {}')
    print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> x /= y')
    print('>>> x')
    x = {}
    y = {"a": 1, "c": 2.3456, "d": "another"}
    x /= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = {}')
    print('>>> x /= y')
    print('>>> x')
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = {}
    x /= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> x /= y')
    print('>>> x')
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = {"a": 1, "c": 2.3456, "d": "another"}
    x /= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
