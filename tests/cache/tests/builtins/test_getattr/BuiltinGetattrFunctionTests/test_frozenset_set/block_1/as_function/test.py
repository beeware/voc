def test_function():
    try:
        print('>>> f = getattr')
        print('>>> x = frozenset()')
        print('>>> y = set()')
        print('>>> f(x, y)')
        f = getattr
        x = frozenset()
        y = set()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = frozenset()')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> f(x, y)')
        f = getattr
        x = frozenset()
        y = {1, 2.3456, "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = set()')
        print('>>> f(x, y)')
        f = getattr
        x = frozenset({1, 2.3456, "another"})
        y = set()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = getattr')
        print('>>> x = frozenset({1, 2.3456, "another"})')
        print('>>> y = {1, 2.3456, "another"}')
        print('>>> f(x, y)')
        f = getattr
        x = frozenset({1, 2.3456, "another"})
        y = {1, 2.3456, "another"}
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()