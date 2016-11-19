try:
    print('>>> x = b""')
    print('>>> y = frozenset()')
    print('>>> x / y')
    x = b""
    y = frozenset()
    print(x / y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = b""')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x / y')
    x = b""
    y = frozenset({1, 2.3456, "another"})
    print(x / y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = b"This is another string of bytes"')
    print('>>> y = frozenset()')
    print('>>> x / y')
    x = b"This is another string of bytes"
    y = frozenset()
    print(x / y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = b"This is another string of bytes"')
    print('>>> y = frozenset({1, 2.3456, "another"})')
    print('>>> x / y')
    x = b"This is another string of bytes"
    y = frozenset({1, 2.3456, "another"})
    print(x / y)
except Exception as e:
    print(type(e), ':', e)
print()
