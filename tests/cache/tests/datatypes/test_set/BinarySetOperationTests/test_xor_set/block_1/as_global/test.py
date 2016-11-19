try:
    print('>>> x = set()')
    print('>>> y = set()')
    print('>>> x ^ y')
    x = set()
    y = set()
    print(x ^ y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = set()')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> x ^ y')
    x = set()
    y = {1, 2.3456, "another"}
    print(x ^ y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = set()')
    print('>>> x ^ y')
    x = {1, 2.3456, "another"}
    y = set()
    print(x ^ y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> x ^ y')
    x = {1, 2.3456, "another"}
    y = {1, 2.3456, "another"}
    print(x ^ y)
except Exception as e:
    print(type(e), ':', e)
print()
