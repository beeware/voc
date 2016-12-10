try:
    print('>>> x = set()')
    print('>>> y = (1, 2)')
    print('>>> x += y')
    print('>>> x')
    x = set()
    y = (1, 2)
    x += y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = set()')
    print('>>> y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
    print('>>> x += y')
    print('>>> x')
    x = set()
    y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    x += y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = set()')
    print('>>> y = (3, 1.2, True, )')
    print('>>> x += y')
    print('>>> x')
    x = set()
    y = (3, 1.2, True, )
    x += y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = set()')
    print('>>> y = (1, 2.3456, "another")')
    print('>>> x += y')
    print('>>> x')
    x = set()
    y = (1, 2.3456, "another")
    x += y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = (1, 2)')
    print('>>> x += y')
    print('>>> x')
    x = {1, 2.3456, "another"}
    y = (1, 2)
    x += y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
    print('>>> x += y')
    print('>>> x')
    x = {1, 2.3456, "another"}
    y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    x += y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = (3, 1.2, True, )')
    print('>>> x += y')
    print('>>> x')
    x = {1, 2.3456, "another"}
    y = (3, 1.2, True, )
    x += y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = (1, 2.3456, "another")')
    print('>>> x += y')
    print('>>> x')
    x = {1, 2.3456, "another"}
    y = (1, 2.3456, "another")
    x += y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
