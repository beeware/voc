def test_function():
    try:
        print('>>> f = getattr')
        print('>>> x = bytearray()')
        print('>>> y = frozenset()')
        print('>>> f(x, y)')
        f = getattr
        x = bytearray()
        y = frozenset()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = bytearray()')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> f(x, y)')
        f = getattr
        x = bytearray()
        y = frozenset({1, 2.3456, "another"})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = bytearray(1)')
        print('>>> y = frozenset()')
        print('>>> f(x, y)')
        f = getattr
        x = bytearray(1)
        y = frozenset()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = bytearray(1)')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> f(x, y)')
        f = getattr
        x = bytearray(1)
        y = frozenset({1, 2.3456, "another"})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = frozenset()')
        print('>>> f(x, y)')
        f = getattr
        x = bytearray([1, 2, 3])
        y = frozenset()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = bytearray([1, 2, 3])')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> f(x, y)')
        f = getattr
        x = bytearray([1, 2, 3])
        y = frozenset({1, 2.3456, "another"})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()