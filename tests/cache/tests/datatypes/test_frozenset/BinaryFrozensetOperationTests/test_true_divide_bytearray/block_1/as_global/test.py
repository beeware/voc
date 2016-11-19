try:
    print('>>> x = frozenset()')
    print('>>> y = bytearray()')
    print('>>> x / y')
    x = frozenset()
    y = bytearray()
    print(x / y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset()')
    print('>>> y = bytearray(1)')
    print('>>> x / y')
    x = frozenset()
    y = bytearray(1)
    print(x / y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset()')
    print('>>> y = bytearray([1, 2, 3])')
    print('>>> x / y')
    x = frozenset()
    y = bytearray([1, 2, 3])
    print(x / y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = bytearray()')
    print('>>> x / y')
    x = frozenset({1, 2.3456, "another"})
    y = bytearray()
    print(x / y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = bytearray(1)')
    print('>>> x / y')
    x = frozenset({1, 2.3456, "another"})
    y = bytearray(1)
    print(x / y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = bytearray([1, 2, 3])')
    print('>>> x / y')
    x = frozenset({1, 2.3456, "another"})
    y = bytearray([1, 2, 3])
    print(x / y)
except Exception as e:
    print(type(e), ':', e)
print()
