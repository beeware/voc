def test_function():
    try:
        print('>>> f = pow')
        print('>>> x = frozenset()')
        print('>>> y = frozenset()')
        print('>>> f(x, y)')
        f = pow
        x = frozenset()
        y = frozenset()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = frozenset()')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> f(x, y)')
        f = pow
        x = frozenset()
        y = frozenset({1, 2.3456, "another"})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = frozenset()')
        print('>>> f(x, y)')
        f = pow
        x = frozenset({1, 2.3456, "another"})
        y = frozenset()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = pow')
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> f(x, y)')
        f = pow
        x = frozenset({1, 2.3456, "another"})
        y = frozenset({1, 2.3456, "another"})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()