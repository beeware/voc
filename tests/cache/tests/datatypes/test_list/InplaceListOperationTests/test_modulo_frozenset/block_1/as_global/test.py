try:
    print('>>> x = []')
    print('>>> y = frozenset()')
    print('>>> x %= y')
    print('>>> x')
    x = []
    y = frozenset()
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = []')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x %= y')
    print('>>> x')
    x = []
    y = frozenset({1, 2.3456, "another"})
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = [3, 4, 5]')
    print('>>> y = frozenset()')
    print('>>> x %= y')
    print('>>> x')
    x = [3, 4, 5]
    y = frozenset()
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = [3, 4, 5]')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x %= y')
    print('>>> x')
    x = [3, 4, 5]
    y = frozenset({1, 2.3456, "another"})
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
    print('>>> y = frozenset()')
    print('>>> x %= y')
    print('>>> x')
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = frozenset()
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x %= y')
    print('>>> x')
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = frozenset({1, 2.3456, "another"})
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = ["a","b","c"]')
    print('>>> y = frozenset()')
    print('>>> x %= y')
    print('>>> x')
    x = ["a","b","c"]
    y = frozenset()
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = ["a","b","c"]')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x %= y')
    print('>>> x')
    x = ["a","b","c"]
    y = frozenset({1, 2.3456, "another"})
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
