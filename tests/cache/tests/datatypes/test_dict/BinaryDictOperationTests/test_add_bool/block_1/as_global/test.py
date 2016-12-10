try:
    print('>>> x = {}')
    print('>>> y = True')
    print('>>> x + y')
    x = {}
    y = True
    print(x + y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {}')
    print('>>> y = False')
    print('>>> x + y')
    x = {}
    y = False
    print(x + y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = True')
    print('>>> x + y')
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = True
    print(x + y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = False')
    print('>>> x + y')
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = False
    print(x + y)
except Exception as e:
    print(type(e), ':', e)
print()
