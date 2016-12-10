try:
    print('>>> f = map')
    print('>>> x = frozenset()')
    print('>>> y = b""')
    print('>>> f(x, y)')
    f = map
    x = frozenset()
    y = b""
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = frozenset()')
    print('>>> y = b"This is another string of bytes"')
    print('>>> f(x, y)')
    f = map
    x = frozenset()
    y = b"This is another string of bytes"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = b""')
    print('>>> f(x, y)')
    f = map
    x = frozenset({1, 2.3456, "another"})
    y = b""
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = map')
    print('>>> x = frozenset({1, 2.3456, "another"})')
    print('>>> y = b"This is another string of bytes"')
    print('>>> f(x, y)')
    f = map
    x = frozenset({1, 2.3456, "another"})
    y = b"This is another string of bytes"
    print(f(x, y))
except Exception as e:
    print(type(e), ':', e)
print()
