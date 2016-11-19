def test_function():
    try:
        print('>>> f = map')
        print('>>> x = set()')
        print('>>> y = frozenset()')
        print('>>> f(x, y)')
        f = map
        x = set()
        y = frozenset()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = set()')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> f(x, y)')
        f = map
        x = set()
        y = frozenset({1, 2.3456, "another"})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = frozenset()')
        print('>>> f(x, y)')
        f = map
        x = {1, 2.3456, "another"}
        y = frozenset()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = map')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> f(x, y)')
        f = map
        x = {1, 2.3456, "another"}
        y = frozenset({1, 2.3456, "another"})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()