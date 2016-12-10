try:
    print('>>> x = bytearray()')
    print('>>> y = frozenset()')
    print('>>> x &= y')
    print('>>> x')
    x = bytearray()
    y = frozenset()
    x &= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = bytearray()')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x &= y')
    print('>>> x')
    x = bytearray()
    y = frozenset({1, 2.3456, "another"})
    x &= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = bytearray(1)')
    print('>>> y = frozenset()')
    print('>>> x &= y')
    print('>>> x')
    x = bytearray(1)
    y = frozenset()
    x &= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = bytearray(1)')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x &= y')
    print('>>> x')
    x = bytearray(1)
    y = frozenset({1, 2.3456, "another"})
    x &= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = bytearray([1, 2, 3])')
    print('>>> y = frozenset()')
    print('>>> x &= y')
    print('>>> x')
    x = bytearray([1, 2, 3])
    y = frozenset()
    x &= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = bytearray([1, 2, 3])')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x &= y')
    print('>>> x')
    x = bytearray([1, 2, 3])
    y = frozenset({1, 2.3456, "another"})
    x &= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
