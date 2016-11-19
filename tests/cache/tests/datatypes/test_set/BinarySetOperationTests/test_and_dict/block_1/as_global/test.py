try:
    print('>>> x = set()')
    print('>>> y = {}')
    print('>>> x & y')
    x = set()
    y = {}
    print(x & y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = set()')
    print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> x & y')
    x = set()
    y = {"a": 1, "c": 2.3456, "d": "another"}
    print(x & y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = {}')
    print('>>> x & y')
    x = {1, 2.3456, "another"}
    y = {}
    print(x & y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> x & y')
    x = {1, 2.3456, "another"}
    y = {"a": 1, "c": 2.3456, "d": "another"}
    print(x & y)
except Exception as e:
    print(type(e), ':', e)
print()
