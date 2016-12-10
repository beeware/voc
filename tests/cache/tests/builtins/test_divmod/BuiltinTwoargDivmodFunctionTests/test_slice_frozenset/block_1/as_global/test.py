try:
    print('>>> f = divmod')
    print('>>> x = slice(0)')
    print('>>> y = frozenset()')
    print('>>> f(x, y)')
    f = divmod
    x = slice(0)
    y = frozenset()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = slice(0)')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> f(x, y)')
    f = divmod
    x = slice(0)
    y = frozenset({1, 2.3456, "another"})
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = slice(5)')
    print('>>> y = frozenset()')
    print('>>> f(x, y)')
    f = divmod
    x = slice(5)
    y = frozenset()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = slice(5)')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> f(x, y)')
    f = divmod
    x = slice(5)
    y = frozenset({1, 2.3456, "another"})
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = slice(2, 7)')
    print('>>> y = frozenset()')
    print('>>> f(x, y)')
    f = divmod
    x = slice(2, 7)
    y = frozenset()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = slice(2, 7)')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> f(x, y)')
    f = divmod
    x = slice(2, 7)
    y = frozenset({1, 2.3456, "another"})
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = slice(2, 7, 2)')
    print('>>> y = frozenset()')
    print('>>> f(x, y)')
    f = divmod
    x = slice(2, 7, 2)
    y = frozenset()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = slice(2, 7, 2)')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> f(x, y)')
    f = divmod
    x = slice(2, 7, 2)
    y = frozenset({1, 2.3456, "another"})
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = slice(7, 2, -1)')
    print('>>> y = frozenset()')
    print('>>> f(x, y)')
    f = divmod
    x = slice(7, 2, -1)
    y = frozenset()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = slice(7, 2, -1)')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> f(x, y)')
    f = divmod
    x = slice(7, 2, -1)
    y = frozenset({1, 2.3456, "another"})
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = slice(7, 2, -2)')
    print('>>> y = frozenset()')
    print('>>> f(x, y)')
    f = divmod
    x = slice(7, 2, -2)
    y = frozenset()
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = divmod')
    print('>>> x = slice(7, 2, -2)')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> f(x, y)')
    f = divmod
    x = slice(7, 2, -2)
    y = frozenset({1, 2.3456, "another"})
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
