try:
    print('>>> f = divmod')
    print('>>> x = {}')
    print('>>> y = (1, 2)')
    print('>>> f(x, y)')
    f = divmod
    x = {}
    y = (1, 2)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = {}')
    print('>>> y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
    print('>>> f(x, y)')
    f = divmod
    x = {}
    y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = {}')
    print('>>> y = (3, 1.2, True, )')
    print('>>> f(x, y)')
    f = divmod
    x = {}
    y = (3, 1.2, True, )
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = {}')
    print('>>> y = (1, 2.3456, "another")')
    print('>>> f(x, y)')
    f = divmod
    x = {}
    y = (1, 2.3456, "another")
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = (1, 2)')
    print('>>> f(x, y)')
    f = divmod
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = (1, 2)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
    print('>>> f(x, y)')
    f = divmod
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = (3, 1.2, True, )')
    print('>>> f(x, y)')
    f = divmod
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = (3, 1.2, True, )
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = (1, 2.3456, "another")')
    print('>>> f(x, y)')
    f = divmod
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = (1, 2.3456, "another")
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
