def test_function():
    try:
        print('>>> f = map')
        print('>>> x = frozenset()')
        print('>>> y = bytearray()')
        print('>>> f(x, y)')
        f = map
        x = frozenset()
        y = bytearray()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = frozenset()')
        print('>>> y = bytearray(1)')
        print('>>> f(x, y)')
        f = map
        x = frozenset()
        y = bytearray(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = frozenset()')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> f(x, y)')
        f = map
        x = frozenset()
        y = bytearray([1, 2, 3])
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = bytearray()')
        print('>>> f(x, y)')
        f = map
        x = frozenset({1, 2.3456, "another"})
        y = bytearray()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = bytearray(1)')
        print('>>> f(x, y)')
        f = map
        x = frozenset({1, 2.3456, "another"})
        y = bytearray(1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = bytearray([1, 2, 3])')
        print('>>> f(x, y)')
        f = map
        x = frozenset({1, 2.3456, "another"})
        y = bytearray([1, 2, 3])
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()