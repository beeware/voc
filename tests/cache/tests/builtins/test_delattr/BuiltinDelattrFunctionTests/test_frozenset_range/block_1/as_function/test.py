def test_function():
    try:
        print('>>> f = delattr')
        print('>>> x = frozenset()')
        print('>>> y = range(0)')
        print('>>> f(x, y)')
        f = delattr
        x = frozenset()
        y = range(0)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = frozenset()')
        print('>>> y = range(5)')
        print('>>> f(x, y)')
        f = delattr
        x = frozenset()
        y = range(5)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = frozenset()')
        print('>>> y = range(2, 7)')
        print('>>> f(x, y)')
        f = delattr
        x = frozenset()
        y = range(2, 7)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = frozenset()')
        print('>>> y = range(2, 7, 2)')
        print('>>> f(x, y)')
        f = delattr
        x = frozenset()
        y = range(2, 7, 2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = frozenset()')
        print('>>> y = range(7, 2, -1)')
        print('>>> f(x, y)')
        f = delattr
        x = frozenset()
        y = range(7, 2, -1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = frozenset()')
        print('>>> y = range(7, 2, -2)')
        print('>>> f(x, y)')
        f = delattr
        x = frozenset()
        y = range(7, 2, -2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = range(0)')
        print('>>> f(x, y)')
        f = delattr
        x = frozenset({1, 2.3456, "another"})
        y = range(0)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = range(5)')
        print('>>> f(x, y)')
        f = delattr
        x = frozenset({1, 2.3456, "another"})
        y = range(5)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = range(2, 7)')
        print('>>> f(x, y)')
        f = delattr
        x = frozenset({1, 2.3456, "another"})
        y = range(2, 7)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = range(2, 7, 2)')
        print('>>> f(x, y)')
        f = delattr
        x = frozenset({1, 2.3456, "another"})
        y = range(2, 7, 2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = range(7, 2, -1)')
        print('>>> f(x, y)')
        f = delattr
        x = frozenset({1, 2.3456, "another"})
        y = range(7, 2, -1)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = range(7, 2, -2)')
        print('>>> f(x, y)')
        f = delattr
        x = frozenset({1, 2.3456, "another"})
        y = range(7, 2, -2)
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()