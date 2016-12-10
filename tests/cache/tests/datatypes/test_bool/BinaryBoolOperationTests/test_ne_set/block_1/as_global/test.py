try:
    print('>>> x = True')
    print('>>> y = set()')
    print('>>> x != y')
    x = True
    y = set()
    print(x != y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = True')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> x != y')
    x = True
    y = {1, 2.3456, "another"}
    print(x != y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = False')
    print('>>> y = set()')
    print('>>> x != y')
    x = False
    y = set()
    print(x != y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = False')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> x != y')
    x = False
    y = {1, 2.3456, "another"}
    print(x != y)
except Exception as e:
    print(type(e), ':', e)
print()
