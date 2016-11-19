def test_function():
    try:
        print('>>> f = delattr')
        print('>>> x = set()')
        print('>>> y = frozenset()')
        print('>>> f(x, y)')
        f = delattr
        x = set()
        y = frozenset()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = set()')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> f(x, y)')
        f = delattr
        x = set()
        y = frozenset({1, 2.3456, "another"})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = frozenset()')
        print('>>> f(x, y)')
        f = delattr
        x = {1, 2.3456, "another"}
        y = frozenset()
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    ##################################################
    try:
        print('>>> f = delattr')
        print('>>> x = {1, 2.3456, "another"}')
        print('>>> y = frozenset({1, 2.3456, "another"})')
        print('>>> f(x, y)')
        f = delattr
        x = {1, 2.3456, "another"}
        y = frozenset({1, 2.3456, "another"})
        print(f(x, y))
    except Exception as e:
        print(type(e), ':', e)
    print()
    
test_function()