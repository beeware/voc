try:
    print('>>> x = range(0)')
    print('>>> y = set()')
    print('>>> x < y')
    x = range(0)
    y = set()
    print(x < y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = range(0)')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> x < y')
    x = range(0)
    y = {1, 2.3456, "another"}
    print(x < y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = range(5)')
    print('>>> y = set()')
    print('>>> x < y')
    x = range(5)
    y = set()
    print(x < y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = range(5)')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> x < y')
    x = range(5)
    y = {1, 2.3456, "another"}
    print(x < y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = range(2, 7)')
    print('>>> y = set()')
    print('>>> x < y')
    x = range(2, 7)
    y = set()
    print(x < y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = range(2, 7)')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> x < y')
    x = range(2, 7)
    y = {1, 2.3456, "another"}
    print(x < y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = range(2, 7, 2)')
    print('>>> y = set()')
    print('>>> x < y')
    x = range(2, 7, 2)
    y = set()
    print(x < y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = range(2, 7, 2)')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> x < y')
    x = range(2, 7, 2)
    y = {1, 2.3456, "another"}
    print(x < y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = range(7, 2, -1)')
    print('>>> y = set()')
    print('>>> x < y')
    x = range(7, 2, -1)
    y = set()
    print(x < y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = range(7, 2, -1)')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> x < y')
    x = range(7, 2, -1)
    y = {1, 2.3456, "another"}
    print(x < y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = range(7, 2, -2)')
    print('>>> y = set()')
    print('>>> x < y')
    x = range(7, 2, -2)
    y = set()
    print(x < y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = range(7, 2, -2)')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> x < y')
    x = range(7, 2, -2)
    y = {1, 2.3456, "another"}
    print(x < y)
except Exception as e:
    print(type(e), ':', e)
print()
